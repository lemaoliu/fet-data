# Fine-grained Entity Typing without Knowledge Base #

This section describes the data format of Pseudo Data and the mapping relationship between Pseudo Data and FIGER dataset and OntoNotes dataset.

## Pseudo Data ##

The data format is as follows. key-"tokens" represents the input tokens of the data, and the original sentence can be obtained by splicing with spaces; key-"mentions" stores each mention and its label in the sentence, and each record contains the start and end position of the mention, and the corresponding label.

```json
{
    "tokens":["Apple", "is", "company", "."],
    "mentions":[
        {"start":0, "end":1, "labels":["org.generic", "org.company"]},
        ...
    ],
    ... ...
}
```

## How to use ##

Use `data_mapping.py` to map the dataset. The commands are as follows:

`python data_mapping.py --inp file1 --out file2 --mapping file3`

- file1: the path of input file待映射的数据文件路径

- file2: the path of output file

- file3: mapping file

## Appendix: Mapping file ##

**mapping_figer.csv** and **mapping_onto.csv** are the mapping tables used in the experiment, each line contains two strings, which are separated by tabs. The first string is the label on the target data (FIGER or OntoNotes), and the second string represents the label on the Pseudo Data.

**If a label of pseudo Data cannot be mapped to the target data, we will map it to an appropriate superclass to ensure the validity of the data.**

**mapping_figer.csv**

```
/art	kafield.art
/art/film	art.genre(film)
/astral_body	astronomy.object
/award	basic.award_type
/biology	life.creature
/body_part	attr.function(body)
/broadcast_network	org.broadcast_network
/broadcast_program	work.broadcast_program
/broadcast/tv_channel	service.tv_channel
/building	arc_structure.building
/building/airport	loc.airport
/building/dam	arc_structure.dam
/building/hospital	org.hospital
/building/hotel	loc.hotel
/building/library	loc.library
/building/power_station	product.device(electronic)
/building/restaurant	loc.restaurant
/building/sports_facility	product.equipment(sports)
/building/theater	arc_structure.theater
/chemistry	chemistry.chemical
/computer/algorithm	computer.algorithm
/computer/programming_language	language.programming
/disease	medicine.disease
/education/department	org.generic(education)
/education/educational_degree	basic.academic_degree
/event	event.generic
/event/attack	event.battle
/event/election	loc.electoral_district
/event/military_conflict	event.war
/event/natural_disaster	event.disaster(natural)
/event/protest	event.battle
/event/sports_event	event.sport
/event/terrorist_attack	event.war
/finance/currency	business.currency
/finance/stock_exchange	loc.stock_exchange
/food	food.generic
/game	activity.game
/geography/glacier	loc.geo.glacier
/geography/island	loc.island
/geography/mountain	land_form.mountain
/god	life.god
/government_agency	org.agency(government)
/government/government	org.government
/government/political_party	org.political_party
/internet/website	computer.web.site
/language	language.human_lang
/law	cognition.law
/living_thing	life.organism
/livingthing/animal	life.animal
/location	loc.generic
/location/body_of_water	loc.body_of_water
/location/bridge	arc_structure.bridge
/location/cemetery	loc.cemetery
/location/city	loc.city
/location/country	loc.country
/location/county	loc.county
/location/province	loc.admin_division.province
/medicine/drug	medicine.drug
/medicine/medical_treatment	medicine.treatment
/medicine/symptom	medicine.symptom
/metropolitan_transit/transit_line	vehicle.bus
/military	basic.unit.military
/music	work.song
/news_agency	ap.news_media
/newspaper	work.publication.newspaper
/organization	org.generic
/organization/airline	org.airline
/organization/company	org.company
/organization/educational_institution	org.generic(education)
/organization/fraternity_sorority	org.college_fraternity_sorority
/organization/sports_league	org.sports_league
/organization/sports_team	org.sports_team
/organization/terrorist_organization	military.force
/park	loc.park
/people/ethnicity	person_group.ethnic_group
/person	person.generic
/person/actor	person.performer.actor
/person/architect	person.architect
/person/artist	person.artist
/person/athlete	person.athlete
/person/author	person.pro.writer
/person/coach	person.sports.coach
/person/director	person.director.art
/person/doctor	person.medical.doctor
/person/engineer	person.architect
/person/monarch	person.royal.monarch
/person/musician	person.musician
/person/politician	person.politician
/person/religious_leader	person.leader(religious)
/person/soldier	person.warrior
/person/terrorist	person.warrior
/play	work.theatre
/product	product.generic
/product/airplane	vehicle.aeroplane
/product/camera	device.camera
/product/car	vehicle.car
/product/computer	device.computer
/product/engine_device	device.engine_motor
/product/instrument	basic.instrument
/product/mobile_phone	device.mobilephone
/product/ship	vehicle.ship
/product/spacecraft	vehicle.spacecraft
/product/weapon	device.weapon
/rail/railway	structure.road.railway
/religion	kafield.religion
/religion/religion	cognition.doctrine(religion)
/software	computer.software
/time	time.generic
/title	basic.title_of_person
/train	vehicle.train
/transit	arc_structure.transit_stop
/transportation/road	structure.road
/visual_art/color	attr.color
/written_work	work.literature_work
```

**mapping_onto.csv**

```
/location	loc.generic			
/location/celestial	astronomy.object			
/location/city	loc.city			
/location/country	loc.country			
/location/geography	loc.geo			
/location/geography/body_of_water	loc.body_of_water			
/location/geography/island	loc.island			
/location/geography/mountain	land_form.mountain			
/location/park	loc.park			
/location/structure	loc.admin_division			
/location/structure/airport	loc.airport					
/location/structure/hotel	loc.hotel			
/location/structure/restaurant	loc.restaurant				
/location/structure/theater	arc_structure.theater	
/location/transit/bridge	arc_structure.bridge			
/location/transit/railway	structure.road.railway			
/location/transit/road	structure.road			
/organization	org.generic			
/organization/company	org.company					
/organization/company/news	org.broadcast_network			
/organization/education	org.generic(education)			
/organization/government	org.government			
/organization/political_party	org.political_party			
/organization/sports_league	org.sports_league			
/organization/sports_team	org.sports_team			
/organization/stock_exchange	loc.stock_exchange				
/other	NONElabel			
/other/art	kafield.art			
/other/art/broadcast	work.broadcast_program			
/other/art/film	art.genre(film)			
/other/art/music	work.song			
/other/art/stage	work.theatre				
/other/award	basic.award_type				
/other/currency	business.currency			
/other/event	event.generic					
/other/event/natural_disaster	event.disaster(natural)				
/other/event/sports_event	event.sport			
/other/event/violent_conflict	event.battle		
/other/health/malady	medicine.disease			
/other/health/treatment	medicine.treatment		
/other/internet	computer.web.site			
/other/language	language.human_lang			
/other/language/programming_language	language.programming			
/other/legal	cognition.law				
/other/living_thing/animal	life.animal			
/other/product	product.generic			
/other/product/car	vehicle.car			
/other/product/computer	device.computer			
/other/product/mobile_phone	device.mobilephone			
/other/product/software	computer.software			
/other/product/weapon	device.weapon			
/other/religion	kafield.religion			
/person	person.generic			
/person/artist	person.artist			
/person/artist/actor	person.performer.actor			
/person/artist/author	person.pro.writer			
/person/artist/director	person.director.art			
/person/artist/music	person.musician			
/person/athlete	person.athlete				
/person/coach	person.sports.coach			
/person/doctor	person.medical.doctor		
/person/political_figure	person.politician			
/person/religious_leader	person.leader(religious)			
/person/title	basic.title_of_person			
/other	activity.game			
/other	arc_structure.building			
/other	arc_structure.dam			
/other	arc_structure.transit_stop			
/other	attr.color			
/other	chemistry.chemical			
/other	computer.algorithm			
/other	device.camera			
/other	device.engine_motor			
/other/event	event.disaster			
/other/event	event.war			
/other	food.generic			
/other	life.creature			
/other	life.god			
/other	life.organism			
/location	loc.admin_division.province			
/location	loc.cemetery			
/location	loc.county			
/location	loc.electoral_district			
/location	loc.geo.glacier			
/location	loc.library			
/other	medicine.drug			
/other	medicine.symptom			
/organization	org.agency(government)			
/organization	org.airline			
/organization	org.college_fraternity_sorority			
/organization	org.hospital			
/other	person.architect			
/person	person.performer			
/person	person.royal.monarch			
/person	person.warrior			
/person	person_group.ethnic_group			
/other	time.generic			
/other	vehicle.ship			
/other	vehicle.spacecraft			
/other	work.literature_work			
/other	work.publication			
/other	work.publication.newspaper	
```





