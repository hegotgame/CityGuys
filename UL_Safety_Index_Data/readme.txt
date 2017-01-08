UL Safety IndexTM Data File
This tab-delimited file provides the data for the UL Safety Index, an algorithm based data science initiative that provides individuals and organizations relevant data they may use to explore safety, inform policy and investment choices and make science-based decisions for a more 
secure, healthier and safer world.  

The file contains indicators, drivers and index values for 187 countries.  The data include the input data as well as the normalized indicators.  For more information about the normalization process and the calculation of the indicators, drivers and index, go to http://www.ulsafetyindex.org.  
Data fields that end in “rating” are the indicators within the index and range from 0 to 100.

Data Definitions
Field Name
Field 
Type
Units
Definition

country
Text
N/A
Name of country based on United Nations country list.

country_slug
Text
N/A
Name of country used to match country to standard names in mapping software.

institutions_resources
Number
N/A
Institutions & Resources Driver.  Range:  0-100.

safety_frameworks
Number
N/A
Safety Frameworks Driver.  Range:  0-100

safety_outcomes
Number
N/A
Safety Outcomes Driver.  Range: 0-100

ul_safety_index	
Number
N/A
UL Safety Index.  Range:  0-100

transport_injuries
Number
DALY/100,000 Population
The number of years of life lived in disability or years lost due to premature death from transport injuries in a country divided by the population of the country.  Range:  258.6508149-3527.887923

transport_injuries_rating
Number
N/A
Transport injuries Indicator.  Calculated by normalizing “transport_injuries” using the min-max method.  Range:  0-100.

falls
Number
DALY/100,000 Population
The number of years of life lived in disability or years lost due to premature death from fall injuries in a country divided by the population of the country.  Range:  53.01527293-1634.584277

falls_rating
Number
N/A
Fall injuries Indicator.  Calculated by normalizing “falls” using the min-max method.  Range:  0-100.

drowning
Number
DALY/100,000 Population
The number of years of life lived in disability or years lost due to premature death from drowning injuries in a country divided by the population of the country.  Range:  17.92248076-1045.018781

drowning_rating
Number
N/A
Drowning injuries Indicator.  Calculated by normalizing “drowing” using the min-max method.  Range:  0-100.

fires_heat_hot_substances
Number
DALY/100,000 Population
The number of years of life lived in disability or years lost due to premature death from injuries due to fires, heat and hot substances in a country divided by the population of the country. Range:  19.14321823-518.3626923


fires_heat_hot_substances_rating
Number
N/A
Fires, Heat and Hot Substances injuries Indicator.  Calculated by normalizing “fires_heat_hot_substances” using the min-max method.  Range:  0-100.

poisonings
Number
DALY/100,000 Population
The number of years of life lived in disability or years lost due to premature death from poisoning injuries in a country divided by the population of the country.  Range:  1.796028643-385.8335424

poisonings_rating
Number
N/A
Poisoning injuries Indicator.  Calculated by normalizing “poisonings” using the min-max method.  Range:  0-100.

exposure_to_mechanical_forces
Number
DALY/100,000 Population
The number of years of life lived in disability or years lost due to premature death from injuries due to exposure to mechanical forces, such as crushing, pinching, etc. in a country divided by the population of the country.  Range:  43.72395285-665.5495911

exposure_to_mechanical_forces_rating
Number
N/A
Exposure to Mechanical Forces injuries Indicator.  Calculated by normalizing “exposure-to-mechanical-forces” using the min-max method.  Range:  0-100.

foreign_body
Number
DALY/100,000 Population
The number of years of life lived in disability or years lost due to premature death from injuries due to foreign bodies, such as choking, in a country divided by the population of the country.  Range:  9.247746087-1601.658649

foreign_body_rating
Number
N/A
Foreign Body injuries Indicator.  Calculated by normalizing “foreign_body” using the min-max method.  Range:  0-100.

unintentional_injuries
Number
DALY/100,000 Population
The number of years of life lived in disability or years lost due to premature death from all unintentional injuries in a country divided by the population of the country.  Range:  782.9060429-6495.524743

other_unintentional_injuries
Number
DALY/100,000 Population
The number of years of life lived in disability or years lost due to premature death from unintentional injuries not covered by other categories in a country divided by the population of the country.  Range: 

other_unintentional_injuries_rating
Number
N/A
Other Unintentional Injuries Indicator.  Calculated by normalizing “other_unintentional_injuries” using the min-max method.  Range:  0-100.

exposure_to_forces_of_nature_disaster
Number
DALY/100,000 Population
The number of years of life lived in disability or years lost due to premature death from injuries caused by exposure to the forces of nature and natural disaster, such as earthquakes, in a country divided by the population of the country.  Range:  0-557.0105562

exposure_to_forces_of_nature_disaster_rating
Number
N/A
Exposure to Forces of Nature, Disaster injuries Indicator.  Calculated by normalizing “exposure_to_forces_of_nature_disaster” using the min-max method.  Range:  0-100.

gdp_per_capita
Number
USD per capita
Gross Domestic Product per capita from The World Bank.  Range:  239.8697314-110664.8403

gdp_per_capita_rating	
Number
N/A
GDP per Capita Indicator.  Calculated by normalizing “gdp_per_capita” using the min-max method.  Range:  0-100.

network_readiness_rating
Number
N/A
Networked Readiness Index Indicator.  Calculated by normalizing “network_readiness” using the min-max method.  Range:  0-100.

government_effectiveness_rating
Number
N/A
Government Effectiveness Indicator.  Calculated by normalizing “government_effectiveness” using the min-max method.  Range:  0-100.

education_rating
Number
N/A
Education Indicator.  Calculated by normalizing “education” using the min-max method.  Range:  0-100.

consumer_protection_survey_rating
Number
N/A
Consumer Protections Indicator.  Calculated by normalizing “consumer_protection_survey” using the min-max method. Range:  0-100.

ul_labor_rights_index_rating
Number
N/A
Labor Protections Indicator.  Calculated by normalizing “ul_labor_rights” using the min-max method.  Range:  0-100.

un_region
Text
N/A
Region of the world based on United Nations classifications.

un_sub_region
Text
N/A
Sub-region of the world based on United Nations classifications.

un_development_status	
Text
N/A
Development status based on United Nations classifications .

who_region
Text
N/A
Region of the world based on World Health Organization classification.

population
Number
persons
Country population.  Range:  55000-1371920000

population_decile
Number
N/A
Each of ten equal groups into which the countries have been divided, based on population.  Decile = 1 corresponds to the top 10% of countries in the world, based on population.  Range:  1-10

population_under_15
Number
N/A
Proportion of youth population of the country, aged 15 and under, based on Population Reference Bureau data. Range:  0.13-0.52

youth_population_group
Number
N/A
Grouping of countries with similar youth population percentages.

population_over_65
Number
N/A
Proportion of elderly population of the country, aged 65 and over, based on Population Reference Bureau data.  Range:  0.01-0.26

older_population_group
Number
N/A
Grouping of countries with similar elder population percentages.

gdp
Number
US Dollars
Gross Domestic Product for the country.  Range: 0-17419000000000


gdp_decile
Number
N/A
Each of ten equal groups into which the countries have been divided based on GDP.  Decile = 1 corresponds to the top 10% of countries in the world, based on GDP.  Range:  1-10

iso_abbreviation
Text
N/A
The abbreviation for the country name, based on the International Standards Organization.

iso_membership
Text
N/A
Membership classification within the International Standards Organization

iec_membership
Text
N/A
Membership classification within the International Electrotechnical Commission

government_effectiveness
Number
N/A
The Government Effectiveness Index from the World Bank.  Range:  -2.21-2.17

education
Number
N/A
The Education Index from the UN Development Programme.  Range:  0.198-5.47

network_readiness
Number
N/A
Networked Readiness Index from the Worldwide Economic Forum.  Range:  2.3-5.98

ul_standards_index
Number
N/A
The UL Standards Index, calculated by scoring countries for participation in international standards activities.  Range:  0-15

ul_standards_index_rating
Number
N/A
Standards Index Indicator.  Calculated by normalizing "ul_standards_index" using the min-max method.  Range:  0-100.

consumer_protection_survey
Number
N/A
A score for consumer protection measures, calculated from the results of the Consumers’ International Consumer Protection Survey.  Range:  0.363636364-1.0

ul_labor_rights
Number
N/A
The UL Labor Rights Index, calculated from a country’s record in protecting laborer’s rights.  Range:  0-100


