
### Upload Headers 
Upload a list of headers to a specified groups. Every user who belongs to this group will be able to use these headers. Please note that every upload will overwrite the previews uploads!  
If you want to know what a header is good for, please read the [headers & footers](#headers--footers) part of the documentation!

#####Type
  + POST

#####Route
  + //api.edmdesigner.com/json/groups/uploadHeaders

#### Parameters (you should post):
   * groupId {String} /REQUIRED/ The id of the group. Note that it has to be a valid MongoDB _id. It's best if you use the values that you got when you listed your groups with the [/json/groups/list](#list-groups) route.
   * headers {Array} /REQUIRED/ The list of headers which the users of the specified group will be able to use. __Please note that if you upload a new list, the old list will be overwrited!__ If you want to know how a header object should look like, pls read [this](#structure) part of the documentation.

####Answer:
An object with two arrays:
  - success {Array} The list of the headers which were successfully added to the group
  - failed {Array} The list of the object: 
    - header {Object} The header which is not valid therefore it was not added to the group
    - error {String} The reason why the header is not valid

Or it can be an error object:
  - err Description of the error {String} or an error code {Number}.

___

### Upload Footers 
Upload a list of footers to a specified groups. Every user who belongs to this group will be able to use these footers. Please note that every upload will overwrite the previews uploads!  
If you want to know what a footer is good for, please read the [headers & footers](#headers--footers) part of the documentation!

#####Type
  + POST

#####Route
  + //api.edmdesigner.com/json/groups/uploadFooters

#### Parameters (you should post):
   * groupId {String} /REQUIRED/ The id of the group. Note that it has to be a valid MongoDB _id. It's best if you use the values that you got when you listed your groups with the [/json/groups/list](#list-groups) route.
   * footers {Array} /REQUIRED/ The list of footers which the users of the specified group will be able to use. __Please note that if you upload a new list, the old list will be overwrited!__ If you want to know how a footer object should look like, pls read [this](#structure) part of the documentation.

####Answer:
An object with two arrays:
  - success {Array} list of the footers which were successfully added to the group
  - failed {Array} list of the object: 
    - footer {Object} The footer which is not valid therefore it was not added to the group
    - error {String} The reason why the footer is not valid

Or it can be an error object:
  - err Description of the error {String} or an error code {Number}.

___

### Upload Headers 
Upload a list of headers to a specified user or users. Please note that every upload will overwrite the previews uploads!  
If you want to know what a header is good for, please read the [headers & footers](#headers--footers) part of the documentation!

#####Type
  + POST

#####Route
  + //api.edmdesigner.com/json/user/uploadHeaders

#### Parameters (you should post):
   * users {Array} /REQUIRED/ List of the ids of the users you want to upload the headers.
   * headers {Array} /REQUIRED/ The list of headers which the selected users will be able to use. __Please note that if you upload a new list, the old list will be overwrited!__ If you want to know how a header object should look like, pls read [this](#structure) part of the documentation.

####Answer:
An object with two arrays:
  - success {Array} list of the users whose successfully got the headers
  - failed {Array} list of the object: 
    - user {String} The id of the user who did not get the headers
    - error {String} The reason why the user did not get the headers
  - badHeaders {Array} list of the object: 
    - header {Object} The header which is not valid therefore it was not added to the users
    - error {String} The reason why the header is not valid

Or it can be an error object:
  - err Description of the error {String} or an error code {Number}.

___

### Upload Footers 
Upload a list of footers to a specified user or users. Please note that every upload will overwrite the previews uploads!  
If you want to know what a footer is good for, please read the [headers & footers](#headers--footers) part of the documentation!

#####Type
  + POST

#####Route
  + //api.edmdesigner.com/json/user/uploadFooters

#### Parameters (you should post):
   * users {Array} /REQUIRED/ List of the ids of the users you want to upload the footers.
   * footers {Array} /REQUIRED/ The list of footers which the selected users will be able to use. __Please note that if you upload a new list, the old list will be overwrited!__ If you want to know how a footer object should look like, pls read [this](#structure) part of the documentation.

####Answer:
An object with two arrays:
  - success {Array} The list of the users whose successfully got the footers
  - failed {Array} The list of the object: 
    - user {String} The id of the user who did not get the footers
    - error {String} The reason why the user did not get the footers
  - badFooters {Array} list of the object: 
    - footer {Object} The footer which is not valid therefore it was not added to the users
    - error {String} The reason why the footer is not valid

Or it can be an error object:
  - err Description of the error {String} or an error code {Number}.

___


##Headers & footers
You can upload headers and footers which your users will be able to use. A header will appear on the top of their templates and the footer will appear on the bottom.
The users won’t be able to edit these two elements or remove them.  
If you upload any header and/or footer, then the affected users have to use one. If you want to have a group of user who don’t have to use any kind of header and/or footer, then do not upload header and/or footer to all of your user ([general upload]()) or upload the group an empty header and/or footer. This way they can choose the empty one and then there will be no header and/or footer on their templates.  
You can upload different kind of headers and/or footers. If you do so than the affected users will be able to choose which header they want to use, but they still have to use one of them.   
A newly created template will get the first uploaded header and/or footer which affected the user who created the template. (The header and/or footer priority is the following: user’s personal headers and/or footers <  user’s group’s headers and/or footers < general headers and/or footers)

There is three different ways to upload headers. You can upload it:
  - to all your user ([general header upload](#upload-headers-2)) 
  - to a specified group ([upload headers to group](#upload-headers)) 
  - to specified user or users ([upload headers to user](#upload-headers-1))

Footers can be uploaded in the same ways:
  - to everyone ([general footer upload](#upload-footers-2))
  - to a specified group ([upload footers to a group](#upload-footers))
  - to specified user or users ([upload footers to users](#upload-footers-1))


### Structure
The representing object fore header or footer should have the following properties:
  - document {Object} /REQUIRED/ it should be a json object (which represent our templates)
    - root /REQUIRED/ There should be the structure of the header or footer
    - generalSettings
  - id {String} /REQUIRED/ this id is what we use for distinguish the headers from each other so __it should be unique!__ Please note that the id you want to use for the users headers should be different from the ids of the general headers or the ids of the user's group's headers. The same is true for the footers.
  - title {Object} it should contains language code - title string pairs. For example: 'en': 'Green-white header'. The title will appear on the dropdown list. If you don't want to use any other localization then pls use the 'en' language code, the default always be the 'en' regardless of the actual languages!  
  - placeholders {Object} it is needed when you want to have more than one supported language on your headers or footers. If you want to know have do the placeholders work pls read the [localization](#localization) part of the [headers & footers](#headers--footers) chapter.

___

### Localization
It is possible to use different localization with the same headers and/or footers but __not required__.  
If you want to support only one language then you should "hardcode" the content of the header or footer to the representing json and it should work perfectly. In that case you do not have to use the placeholders object (see [stucture](#structure)).  
If you want to support more than one language, then you have to use the placeholders object. You should not write the actual content to the json instead you should use a placeholder. You can give any kind of name to this placeholder, but it should begin and end with two '#' character (for example: ##title##). After that yous have to insert the placeholder to the placeholders object as follows: the key should be the name of the placeholder , and the value should be an object conatining the language code - value pairs of the actual content.  
Example placeholders object: 

	placeholders: { '##title##': {
				'en': 'The header is a good thing',
				'hu': 'A fejléc egy jó dolog',
				//...
			},
	 '##example-palceholder##: {
	 			'en': 'It is an example',
	 			'hu': 'Ez egy példa',
	 			//...
	 			}
	 }
	 
You can localize the name (title) of the headers and/or footers too. The title of a header is the text which will appear on the dropdown list, where the user will be able to choose which of the given headers and/or footers they want to use.  
If you want to support more than one language you just have to put the language code - text pair to the title object (see [structure](#structure)).
An example title object: 

	title: { 'en': 'example title',
		 'hu': 'példa cím'
		 /...
		}
		
If you support a language but you do not want to give the header or footer a different title in the other language, you do not have to, but please not that this way the default title will be used on the dropdown list for this header , and the default is always the 'en' (english) version of the title.  

Example:  
_We support the english and the hungarian languages. We upload two headers with the following two title objects: title: {'en': 'first 	header'} and title: {'en': 'second header', 'hu': 'Második fejléc'}. If someone select the hungarian language then in his/her dropdown 		list there will be two selectable header: 'first header' and 'Második fejléc', but if someone choose the english version then 		the dropdown list will look like the following: 'first header' and 'second header'._  

If you do not give an 'en' (english) title to a header, then it will be generated automatically in our application, so it is suggested to always upload an 'en' version of the title too.

___

### Upload Headers 
Upload a list of headers which __all of your users__ will be able to use. Please note that every upload will overwrite the previews uploads!  
If you want to know what a header is good for, please read the [headers & footers](#headers--footers) part of the documentation!

#####Type
  + POST

#####Route
  + //api.edmdesigner.com/json/general/uploadHeaders

#### Parameters (you should post):
   * headers {Array} The list of headers which all of your users will be able to use. __Please note that if you upload a new list, the old list will be overwrited!__ If you want to know how a header object should look like, pls read [this](#structure)

####Answer:
An object with two arrays:
  - success {Array} The list of the headers which were successfully saved
  - failed {Array} The list of the object: 
    - header {Object} The header which is not valid therefore it was not saved
    - error {String} The reason why the header is not valid

Or it can be an error object:
  - err Description of the error {String} or an error code {Number}.

___

### Upload Footers 
Upload a list of footers which __all of your users__ will be able to use. Please note that every upload will overwrite the previews uploads!  
If you want to know what a footer is good for, please read the [headers & footers](#headers--footers) part of the documentation!

#####Type
  + POST

#####Route
  + //api.edmdesigner.com/json/general/uploadFooters

#### Parameters (you should post):
   * footers {Array} The list of footers which all of your users will be able to use. __Please note that if you upload a new list, the old list will be overwrited!__ If you want to know how a footer object should look like, pls read [this](#structure) part of the documentation.

####Answer:
An object with two arrays:
  - success {Array} The list of the footers which were successfully saved
  - failed {Array} The list of the object: 
    - footer {Object} The footer which is not valid therefore it was not saved
    - error {String} The reason why the footer is not valid

Or it can be an error object:
  - err Description of the error {String} or an error code {Number}.

___


