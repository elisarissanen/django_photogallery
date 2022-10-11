# subaru-letit

* Elisa Rissanen
* Mitro Latosuo
* Simo Heinonen

The project aims to create a web application, which is built on top of a relational database using a web framework. The projects are done as group work in teams of 2-3 people.

The topics of the project are presented below.

The web application should be implemented so that it is reasonably secure and it works ok on all the most popular browsers, including both desktop browsers (Chrome, Firefox) and mobile browsers (Android Chrome, iOS Safari). Implement the user interface so that it works with the most popular screen resolutions and does not rely solely on keyboard, mouse or touch screen events, i.e. so that it works both on a touch screen device, e.g. a smartphone, and also on a traditional desktop computer.

Each of the web applications must include at the following functionality:
login
create new user (not using administration interface)
logout
You can use Django's ready-made authentication services and Python packages/modules from Pypy. Don’t try to reinvent the wheel!

The application created as a result of the project will be returned and presented to other students and students must also create a report.

Photo gallery
The user, who is logged in, can upload bitmap images to the server in different folders, at least in the following file formats: JPEG, PNG and GIF. The system automatically creates a JPEG preview icon (thumbnail) from the image and can scale the images to a suitable resolution. This can be done by using e.g., the Pillow library or some thumbnail library e.g. sorl-thumbnail. The user can at minimum also view and delete images. Images can be associated with metadata, e.g., text description and tags.

Will it be possible to arrange the pictures? Will it be possible to search images based on tags?
