# Features

* A simple base class for a `form block`
* Leaves the implementation of a `form_valid` up to the developer
* Form content is `StreamBlock` based, and entirely flexible
* Forms can be created entirely in-page, or simply referenced through a `Form chooser block`
* The developer specifies the minimal fields needed to function
* These minimal fields will be validated in the admin
* The structure of the form, and additional fields, are entirely up to the CMS user
* Form content can include any wagtail block, not just ones representing fields
* Multiple forms can coexist on any page or other `StreamField` enabled object, and feedback is presented individually
* Support for field- and form based *clean* methods
* Optional support for a more traditional *success_url* type form handling
* Access to *form_success* and *form_submitted* variables in form template context
