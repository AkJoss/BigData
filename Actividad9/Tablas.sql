create database gans;
use gans;

drop table if exists city_pop;
create table if not exists city_pop(
	city varchar(255),
	country varchar(255),
	country_code varchar(3),
	population decimal,
    elevation_meters decimal,
    latitude decimal,
    longitude decimal,
	municipality_iso_country varchar(255),
    primary key(municipality_iso_country)
);  

drop table if exists airport;
create table if not exists airport(
	airport_name varchar(255),
    latitude_deg decimal,
    longitude_deg decimal,
    elevation_ft decimal,
    iso_country varchar(3),
    iso_region varchar(255),
    municipality varchar(255),
    icao_code varchar(255),
    iata_code varchar(255),
    municipality_iso_country varchar(255),
    primary key(icao_code),
    foreign key (municipality_iso_country) references city_pop(municipality_iso_country)
);


drop table if exists weather_data;
create table if not exists weather_data(
	weather_id int auto_increment,
	weather_datetime datetime,
    temperature decimal,
    humidity integer,
    weather_status varchar(255),
    wind decimal,
    rain_qty decimal,
    snow decimal,
    municipality_iso_country varchar(255),
    primary key(weather_id),
    foreign key(municipality_iso_country) references city_pop(municipality_iso_country)
);

drop table if exists flight_arrival;
create table if not exists flight_arrival(
	arrival_id int auto_increment,
	scheduled_arrival_time datetime,
    flight_number varchar(255),
    from_airport varchar(255),
    airline varchar(255),
    aircraft varchar(255),
    icao_code varchar(255),
    primary key(arrival_id),
    foreign key(icao_code) references airport(icao_code)
);

USE gans;
SELECT * FROM weather_data LIMIT 10;
