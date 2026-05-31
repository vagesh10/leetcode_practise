select Person.firstName,Person.lastName,
Address.city,Address.state from Person Left JOIN Address 
ON Person.personId = Address.personId;
