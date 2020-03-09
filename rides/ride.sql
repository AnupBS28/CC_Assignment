CREATE TABLE Rides ( 
	rideID INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT, 
	timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
	source INTEGER NOT NULL,
	destination INTEGER NOT NULL,
	uname NVARCHAR(50) NOT NULL
);
CREATE TABLE joinedRides( 
	rideID INTEGER  NOT NULL,
	uname NVARCHAR(50) NOT NULL,
	PRIMARY KEY (rideID,uname), 
	FOREIGN KEY (rideId) REFERENCES Rides(rideId) ON DELETE CASCADE	
);

