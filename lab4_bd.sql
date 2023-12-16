DROP DATABASE IF EXISTS my_bd_lab;

CREATE DATABASE IF NOT EXISTS my_bd_lab;
USE my_bd_lab;

CREATE TABLE  city (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_name` (`name` ASC)
) ENGINE = InnoDB;

CREATE TABLE  street (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `city_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_name` (`name` ASC),
  INDEX `fk_street_city1_idx` (`city_id` ASC) VISIBLE,
  CONSTRAINT `fk_street_city1`
    FOREIGN KEY (`city_id`)
    REFERENCES `my_bd_lab`.`city` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;


CREATE TABLE  office (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_name` (`name` ASC)
) ENGINE = InnoDB;

CREATE TABLE  building (
  `id` INT NOT NULL AUTO_INCREMENT,
  `office_id` INT NOT NULL,
  `street_id` INT NOT NULL,
  `building_number` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_building_office1_idx` (`office_id` ASC) VISIBLE,
  INDEX `idx_building_number` (`building_number` ASC),
  CONSTRAINT `fk_building_office1`
    FOREIGN KEY (`office_id`)
    REFERENCES `my_bd_lab`.`office` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_building_street1`
    FOREIGN KEY (`street_id`)
    REFERENCES `my_bd_lab`.`street` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;


CREATE TABLE  floor (
  `id` INT NOT NULL AUTO_INCREMENT,
  `building_id` INT NOT NULL,
  `number` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_floor_building1_idx` (`building_id` ASC) VISIBLE,
  INDEX `idx_number` (`number` ASC),
  CONSTRAINT `fk_floor_building1`
    FOREIGN KEY (`building_id`)
    REFERENCES `my_bd_lab`.`building` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

CREATE TABLE  workplace (
  `id` INT NOT NULL AUTO_INCREMENT,
  `floor_id` INT NOT NULL,
  `workplace_name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_workplace_floor1_idx` (`floor_id` ASC) VISIBLE,
  INDEX `idx_workplace_name` (`workplace_name` ASC),
  CONSTRAINT `fk_workplace_floor1`
    FOREIGN KEY (`floor_id`)
    REFERENCES `my_bd_lab`.`floor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

CREATE TABLE  employee (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `surname` VARCHAR(50) NOT NULL,
  `phone_number` VARCHAR(50) NULL,
  `workplace_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_surname` (`surname` ASC) ,
  INDEX `idx_phone_number` (`phone_number` ASC),
  CONSTRAINT `fk_employee_workplace1`
    FOREIGN KEY (`workplace_id`)
    REFERENCES `my_bd_lab`.`workplace` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

CREATE TABLE  vendor (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `address` VARCHAR(45) NULL,
  `number_phone` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_name` (`name` ASC),
  INDEX `number_phone` (`number_phone` ASC)
) ENGINE = InnoDB;

CREATE TABLE  type (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_name` (`name` ASC)
) ENGINE = InnoDB;

CREATE TABLE equipment (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `serial_number` VARCHAR(45) NULL,
  `employee_id` INT NOT NULL,
  `workplace_id` INT NOT NULL,
  `type_id` INT NOT NULL,
  `vendor_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `idx_name` (`name` ASC) ,
  INDEX `idx_serial_number` (`serial_number` ASC),
  CONSTRAINT `fk_equipment_employee`
    FOREIGN KEY (`employee_id`)
    REFERENCES `my_bd_lab`.`employee` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_equipment_workplace1`
    FOREIGN KEY (`workplace_id`)
    REFERENCES `my_bd_lab`.`workplace` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_equipment_type1`
    FOREIGN KEY (`type_id`)
    REFERENCES `my_bd_lab`.`type` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_equipment_vendor1`
    FOREIGN KEY (`vendor_id`)
    REFERENCES `my_bd_lab`.`vendor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE  department (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `date_create` DATE NOT NULL,
  `employee_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_department_employee1_idx` (`employee_id` ASC) VISIBLE,
  INDEX `idx_date_create` (`date_create` ASC),
  CONSTRAINT `fk_department_employee1`
    FOREIGN KEY (`employee_id`)
    REFERENCES `my_bd_lab`.`employee` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;


-- Додавання даних до таблиць city, street, office, building, floor, workplace, employee, vendor, type
INSERT INTO city ( name) VALUES
('Lviv'),
('Ternopil'),
('Kyiv'),
('Odesa'),
('Vinnytsia'),
('Lytsk'),
('Zhytomyr'),
('Chernivtsi'),
('Chernihiv'),
('Khmelnytskyi');

INSERT INTO street (name, city_id) VALUES
('Horodotska', 1),
('Castle', 2),
('Khreschatyk', 3),
('Seaside Boulevard', 4),
('City Center Drive', 5),
('Township Lane', 6),
('Zhytomyr Street', 7),
('Chernivtsi Road', 8),
('Chernihiv Square', 9),
('Khmelnytskyi Avenue', 10);

INSERT INTO office (name) VALUES
('Office1'),
('Office2'),
('Office3'),
('Office4'),
('Office5'),
('Office6'),
('Office7'),
('Office8'),
('Office9'),
('Office10');

INSERT INTO building (office_id, street_id, building_number) VALUES
(5, 1, 56),
(3, 2, 12),
(8, 3, 23),
(10, 5, 15),
(1, 4, 107),
(4, 7, 51),
(7, 10, 98),
(2, 9, 18),
(6, 8, 31),
(9, 6, 63);

INSERT INTO floor (building_id, number) VALUES
(5, 1),
(3, 12),
(8, 23),
(10, 5),
(1, 4),
(4, 7),
(7, 10),
(2, 18),
(6, 8),
(9, 6);

INSERT INTO workplace (floor_id, workplace_name) VALUES
(5, 'Name1'),
(10, 'Name2'),
(3, 'Name3'),
(9, 'Name4'),
(6, 'Name5'),
(1, 'Name6'),
(4, 'Name7'),
(2, 'Name8'),
(3, 'Name9'),
(7, 'Name10');

INSERT INTO employee (name, surname, phone_number, workplace_id) VALUES
('John', 'Doe', '123-456-7890', 1),
('Jane', 'Smith', '987-654-3210', 2),
('Michael', 'Johnson', '555-123-4567', 3),
('Emily', 'Williams', '444-789-1230', 4),
('David', 'Brown', '222-333-4444', 5),
('Sarah', 'Davis', '111-999-8888', 6),
('Robert', 'Jones', '777-888-9999', 7),
('Megan', 'Miller', '888-777-6666', 8),
('William', 'Wilson', '666-555-4444', 9),
('Olivia', 'Taylor', '333-111-0000', 10);

INSERT INTO vendor (name, address, number_phone) VALUES
('HP', '1 Market Square, Lviv, 79008', '+380933899279'),
('Samsung', '123 Suburban Street, Lviv, 79000', '+380932648910'),
('Canon', '78 Sahaidachnoho Street, Ternopil, 46001', '+380098852647'),
('iPhone', '90 Deribasivska Street, Odesa, 65000', '+380671503386'),
('Cisco', '72 Volodymyrska Street, Kyiv, 01001', '+380559872549'),
('Dell', '25 Oak Avenue, Vinnytsia, 21000', '+380991234567'),
('Lenovo', '50 Pine Street, Lytsk, 43000', '+380777777777'),
('Sony', '15 Elm Road, Zhytomyr, 10000', '+380888888888'),
('Fujitsu', '35 Maple Lane, Chernivtsi, 58000', '+380555555555'),
('Acer', '100 Cedar Court, Chernihiv, 61000', '+380666666666');

INSERT INTO type (name) VALUES
('monitor'),
('laptop'),
('phone'),
('tablet'),
('desktop'),
('server'),
('router'),
('printer'),
('scanner'),
('smartwatch');

INSERT INTO equipment (name, serial_number, employee_id, workplace_id, type_id, vendor_id) VALUES
('Laptop1', 'SN123', 1, 10, 1, 10),
('Monitor2', 'SN456', 1, 9, 2, 9),
('Phone3', 'SN789', 3, 8, 3, 8),
('Desktop4', 'SN101', 4, 7, 4, 7),
('Printer5', 'SN112', 5, 6, 5, 6),
('Server6', 'SN131', 6, 5, 6, 5),
('Tablet7', 'SN141', 7, 4, 7, 4),
('Router8', 'SN151', 8, 3, 8, 3),
('Scanner9', 'SN161', 9, 2, 9, 2),
('Smartwatch10', 'SN171', 10, 1, 10, 1);


INSERT INTO department (name, date_create, employee_id) VALUES
('HR Department', '2023-01-15', 1),
('Finance Department', '2023-02-20', 2),
('Marketing Department', '2023-03-25', 3),
('IT Department', '2023-04-30', 4),
('Sales Department', '2023-05-10', 5),
('R&D Department', '2023-06-15', 6),
('Customer Support Department', '2023-07-20', 7),
('Legal Department', '2023-08-25', 8),
('Logistics Department', '2023-09-30', 9),
('Quality Assurance Department', '2023-10-05', 10);


