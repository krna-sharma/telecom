create database telecom;

use telecom;

CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cust_name VARCHAR(255) NOT NULL,
    dob CHAR(8) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    adhar_number CHAR(12) NOT NULL UNIQUE,
    registration_date DATE  DEFAULT (CURRENT_DATE()),
    assigned_mobile_number CHAR(10) NOT NULL UNIQUE
);

CREATE TABLE plan_details (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    plan_name VARCHAR(20) NOT NULL,
    plan_cost INT NOT NULL,
    plan_validity INT NOT NULL,
    plan_status VARCHAR(10) NOT NULL,
    CHECK (plan_name IN ('Platinum365', 'Gold180', 'Silver90')),
    CHECK (plan_cost IN (499, 299, 199)),
    CHECK (plan_validity IN (365, 180, 90)),
    CHECK (plan_status IN ('Active', 'Inactive'))
);

INSERT INTO plan_details (plan_name, plan_cost, plan_validity, plan_status) VALUES
('Platinum365', 499.00, 365, 'Active'),
('Gold180', 299.00, 180, 'Active'),
('Silver90', 199.00, 90, 'Active');


CREATE TABLE CustomerPlan (
    email VARCHAR(255) NOT NULL,
    plan_name VARCHAR(20) ,
    renewal_date DATE NULL,
    plan_status ENUM('Active', 'Inactive') NULL
);


DELIMITER //

CREATE TRIGGER set_renewal_date_and_status
BEFORE INSERT ON CustomerPlan
FOR EACH ROW
BEGIN
    DECLARE plan_validity INT;

    -- Get the validity from PlanDetails
    SELECT validity INTO plan_validity FROM PlanDetails WHERE id = NEW.plan_id;

    -- Set the renewal_date
    SET NEW.renewal_date = DATE_ADD(CURDATE(), INTERVAL plan_validity DAY);

    -- Set the plan_status
    IF NEW.renewal_date < CURDATE() THEN
        SET NEW.plan_status = 'Inactive';
    ELSE
        SET NEW.plan_status = 'Active';
    END IF;
END //

DELIMITER ;

