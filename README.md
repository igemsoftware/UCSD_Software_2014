*****
Below is the organization of the SBiDer project and brief summary of its component parts.
*****

**********
PigeonToPNG
**********
	Java project used to create PigeonCAD SBOL visuals from database entries of operons.
**********
-----
**********



**********
Modeling
**********
	Python scripts that interpret characterization data of operons in SBiDer database in 			order to model the synthetic genetic devices behavior. Used by the main application to 			create models of entire genetic circuit behavior.
**********
-----
**********



**********
CircuitNetwork
**********
	*****
	nbproject
	*****
		Project files required to test SBiDer in the Netbeans IDE.
	*****
	-----
	*****



	*****
	src
	*****
		***
		java/communication
		***
			Java servlets connecting the main application to the other components 					such as data retrieval from the database and conversion of data into 					SBOL visuals using PigeonToPNG.
		***
		---
		***



		***
		lib
		***
			A library containing all the .jar files used by SBiDer.
		***
		---
		***
	*****
	-----
	*****



	*****
	web
	*****
		Contains directories for the main application and files for the website 				structure.
		
		Python methods for converting database information into SBML files are stored 				here.
 
		The SBiDer database is stored here as "sbider.db" in addition to the
		Python methods used to access the information. "sbider_network_builder.py" 				creates files used to render the network visually in the main application.

		***
		ProfilePics
		***
			Stores profile images used in the website "About" page.
		***
		---
		***



		***
		WEB-INF
		***
			Contains mapping for the servlets and properties of the testing server
			used during SBiDer web development.
		***
		---
		***



		***
		pigeonImages
		***
			Stores SBOL visuals of all operons in the database to be used by the main
			application during queries or network exploration.
		***
		---
		***



		***
		SBML_TXT_FILES
		***
			Stores the SBML files characterizing the database operons.
		***
		---
		***



		***
		cyjs-sample
		***
			Directory containing the SBiDer application that was built upon the 					CyNetShare project developed by the creators of CytoscapeJS.

			Contains files used to test and develop the project in Yeoman.

			*
			app
			*
				The SBiDer application is here. The "index.html" is controlled 						and modelled by "main.js" and "main.html" respectively. 
			*
			-
			*



			*
			test
			*
				Files run to test CyNetShare.
			*
			-
			*
		***
		---
		***

	*****
	-----
	*****
**********
-----
**********
