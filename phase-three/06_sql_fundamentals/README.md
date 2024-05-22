# SQL Fundamentals & Table Relations

## SWBATs

- [ ] Explain why we use databases
- [ ] Explain what SQL is and why we use it
- [ ] Explain the differences between rows and columns in a table
- [ ] Explain the differences between a Foreign key and a Primary key
- [ ] Explain what a join table is
- [ ] Explain what it means to seed a database
- [ ] Observe using SQL to communicate with a database

---

## Deliverables

#### 1. Select specific columns
<br />

#### 2. Create new database structure
##### 2a. Remove owners table
##### 2b. Create owners table
##### 2c. Create pets table
<br />

#### 3. Modify pets table
##### 3a. Add image_url to pets
##### 3b. Rename column
<br />

#### 4. Create new instances
##### 4a. create owners
##### 4b. create sample data for pets
<br />

#### 5. Read data
##### 5a. Get all columns from pets
##### 5b. Select pet by name
##### 5c. Select pets by favorite treats
##### 5d. Select pets by age 
<br />

#### 6. Update data
##### 6a. Update pet's age by name
##### 6b. Update multiple pets' favorite_treats
<br />

#### 7. Delete data
<br />

#### 8. Join data 
##### 8a. One to many
##### 8b. Many to many: create procedures table 
##### 8c. Many to many: create appointments table
<br />

#### 9. Seed data
##### 9a. Create two procedures
##### 9b. Create six appointments
<br />

#### 10. Join tables
#### 10a. Basic join
#### 10b. Basic join with specific values
#### 10c. Inner join
#### 10d. Outer join


-- SQLite
-- ✅ 1. Select specific columns

-- ✅ 2. Create new database structure

-- ✅ 2a. Remove owners table


-- ✅ 2b. Create owners table

-- ✅ 2c. Create pets table


-- ✅ 3. Modify pets table

-- ✅ 3a. Add image_url to pets

-- ✅ 3b. Rename column

-- ✅ 4. Create data

-- ✅ 4a.create random owners

-- ✅ 4b.create sample data for pets

-- ✅ 5. Read data

-- ✅ 5a. Get all columns from pets

-- ✅ 5b. Select pet by name

-- ✅ 5c. Select pets by favorite treats
-- ✅ 5d. Select pets by age 


-- ✅ 6. Update data
-- ✅ 6a. Update pet's age by name


-- ✅ 6b. Update multiple pets' favorite_treats

-- ✅ 7. Delete data


-- ✅ 8. Join data 
-- ✅ 8a. One to many
-- pets belongs to owner
-- owners has many pets
-- where self.id is in Owner class 
-- python: list comprehension [pet for pets in Pet.all if pet.owner_id=self.id]

-- JOIN...ON...

-- all the appointments for a pet
--how many appts does an owner have
--group by
--count
--multiple JOINS for many to many