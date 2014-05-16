There is an ever-expanding [list](#feature-switch) of possible features which you can choose from.


###Configure api server's gallery
Configure the api's gallery.

#####Type
  + POST

#####Route
  + //api.edmdesigner.com/json/gallery/config
  
#### Parameters (you should post):
  * uploadRoute {String} /REQUIRED/ The route which we can use for uploading the images. (This route should be implemented on your server.)
  * deleteRoute {String} /REQUIRED/ The route which we can use for deleting the images. (This route should be implemented on your server.)
  * noUploadText {Object} It contains the language code (see [available languages](#available-languages)) - html(string) pairs. The given content will be displayed if the upload is not allowed. 
  * limitReached {Object} It contains the language code (see [available languages](#available-languages)) - html(string) pairs. The given content will be displayed if a user reached the upload limit. It is not required to impose a limit on the upload. If you want to know how you can set the limit, please read the [feature switch](#feature-switch) chapter.
  * noUrl {Boolean} With this boolean you can forbid the image handling from absolute urls. If you set this parameter true, then none of your users will be able to use images from absoulte url.

  
Feature Switch
---------------
You can allow or forbid some feature of our application to a group of your users.
The list of the features you can set at the moment:  
  - gallery {Object}: contains the features of the gallery
    - noUpload {Boolean} If you set this parameter true then the users belong to this group cannot use the upload functionality. If you configured the gallery noUploadText (see [gallery config](#configure-api-server)) text then it will appear on the upload tab, otherwise a default text will be used.
    - noUrl {Bollean} If you set this parameter true, then the users of this group cannot use any image not hosted by you. The image from url tab of the gallery will disappear if the feature does not allowed.
    - limit {Number} The number of images the user can upload. If you do not want to set any limit then leave this parameter undefined. If a user reach the limit, then he won't be able to upload any more image and if you configured the gallery limitReached (see [gallery config](#configure-api-server)) text then it will be displayed otherwise a default text will be used.  Please note that the 0 limit and the noUpload are almost equivalent expect a different message will appear on the upload tab if you use one or the other.

This list is constantly expanding with time!
