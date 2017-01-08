'use strict';

var AWS = require('aws-sdk');
var watson = require('watson-developer-cloud');
var keywords = require('./keywords.json');

var docClient = new AWS.DynamoDB.DocumentClient();
var s3 = new AWS.S3();


exports.handler = function(event, context, callback) {


console.log(keywords.locals[0].Department);

var uniqueID = new Date().valueOf();
var cityContacts;

var DynamoDBParams;

var alchemy_language = watson.alchemy_language({
  api_key: 'fc3b7e95e5c9c6e87bc5a7252f43be857df7de10'
})

var bucketKey = event.city + "_" + event.state + ".json";
console.log(bucketKey);

var fileParams = {
  Bucket: 'citycontacts', /* required */
  Key: bucketKey, /* required */
};


s3.getObject(fileParams, handleS3InputValue);

// do all of these callbacks in sync
function handleS3InputValue(err,data) {
   if (err) 
   {
     console.log(err, err.stack); // an error occurred
     callback({"msg":"Contact information for the city does not exist", "exists":false});
   } else {
   
  var AlchemyParameters = {
   extract: 'entities,taxonomy,keywords,doc-sentiment',
   sentiment: 1,
   maxRetrieve: 1,
   text: event.feedback
  };

  cityContacts  = JSON.parse(data.Body.toString());

  console.log("Recieved Data as " + cityContacts.City[0].department);
  alchemy_language.combined(AlchemyParameters, handleIBMResponse);

  }

}

function handleIBMResponse(err, response) 
{
  if (err)
  {
    console.log('error:', err);

  } else {
    console.log(JSON.stringify(response, null, 2));
    
    if(response.status === "OK"){

    console.log("Now performing Key Search");

      var responseVals = response.taxonomy;
      var flag = false;
      for(var val in responseVals)
      {
         console.log(responseVals[val].label);

         var match = searchForKey(responseVals[val].label);
         console.log(match);
         
         if(match != null){
           flag = true;
           var details = retrieveContactDetails(match.Department);
           console.log("Value is " + details);

             DynamoDBParams = {
             TableName:"city-feedback",
             Item: { "ID": uniqueID, 
             "Feedback": event.feedback, 
             "City": event.city, 
             "State": event.state, 
             "Area":event.area,
             "Sentiment":response.docSentiment.type,
             "Department": details.department,
             "Verbose":details.verbose,
             "Info": details
             }
            };

             docClient.put(DynamoDBParams, handleDynamoDBUpload); 
             break;   
          }
      }
      
      if(!flag)
      {
         DynamoDBParams = {
             TableName:"city-feedback",
             Item: { "ID": uniqueID, 
             "Feedback": event.feedback, 
             "City": event.city, 
             "State": event.state, 
             "Area":event.Area,
             "Sentiment":response.docSentiment.type,
             "Department": "GEN"
             }
            };

             docClient.put(DynamoDBParams, handleDynamoDBUpload); 
      }

      
    }
  
  
  
  
  }

}

function handleDynamoDBUpload(err, response) 
{
  console.log(DynamoDBParams);

    if (err) {
        console.error("Unable to add item. Error JSON:", JSON.stringify(err, null, 2));
        callback("Unable to Add Item to DB"); // SUCCESS with message
    } else {
        console.log("Added item:", JSON.stringify(DynamoDBParams, null, 2));
        callback(null, DynamoDBParams); // SUCCESS with message
    }
}

function searchForKey(key){

  var keywordLocals = keywords.locals;

  for(var local in keywordLocals) {

    for(var ibmKey in keywordLocals[local].Taxonomy) {

      if(key === keywordLocals[local].Taxonomy[ibmKey]){
       
        return keywordLocals[local];
      }
    }

    for(var keyword in keywordLocals[local].Keywords) {
       if(key === keywordLocals[local].Keywords[keyword] ) {
        return keywordLocals[local];
      }
    }
  }

  return null;
}

function retrieveContactDetails(key){

  for(var cityGuy in cityContacts.City) {
     console.log(cityContacts.City[cityGuy] + " vs " + key);
    if(cityContacts.City[cityGuy].department === key)
    {
      return cityContacts.City[cityGuy];
    }
  }
}

};

