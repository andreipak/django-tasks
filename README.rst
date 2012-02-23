==============================
42 Coffee Cups Test Assignment
==============================

Tasks
=====

 1. ticket:1 ``base`` Create basic django project that would present your name, surname, bio, contacts on the main page.

  * Data should be stored in the DB, that's
  * `manage.py syncdb`
  * `manage.py runserver`
  * open the browser and all data are in, loaded from fixtures.
  * Use pip **requirements** and **virtualenv** to manage your third party packages dependencies
  * There should be `Makefile` with `test` target running your tests (`make test` to verify it)
  * Mockup: http://framebox.org/Awq-bCzXsh

 2. ticket:3 ``middleware&lists`` Create middleware that stores all http requests in the DB

  * Also, on a separate page show first 10 http requests that are stored by middleware
  * Mockup: http://framebox.org/Awv-QVXKyN

 3. ticket:4 ``template context`` Create template-context-processor that adds django.settings to the context
 4. ticket:5 ``forms&auth`` Create page with form that allows to edit data, presented on the main page

  * Add auth to this page.
  * Upload and show photo.
  * Upload your photo with a towel to your test server on getBarista.
  * Mockups:

   - http://framebox.org/wsv-tfwFbz
   - http://framebox.org/wSk-YPMrdM

 5. ticket:6 ``forms-widgets&jquery`` For birth date on the same page add calendar widget

  * Create own `django widget`_
  * Make this form ajax, using jquery.forms

   - submit form via ajax
   - indicate loading state
   - disable form during submit, so nothing could be entered/changed there

  * Add birthday to main page.
  * Mockup: http://framebox.org/Awr-CQiBTD

 6. ticket:7 ``forms-model-extra`` Let input fields order be reversed

  * All previous tasks where implemented using `forms.ModelForm`? ;)
  * let input fields order be reversed
  * Mockup: http://framebox.org/Aws-cNPUZo

 7. ticket:8 ``template-tags`` Create tag that accepts any object and renders the link to its admin edit page (`{% edit_link request.user %}`)

  * Mockup: http://framebox.org/AwS-tsQHP

 8. ticket:9 ``commands`` Create django command that prints all project models and the count of objects in every model

  Also:

   * duplicate output to STDERR with prefix "error: "
   * write bash script which execute your command and save output of stderr into file. File name should be current date with extension .dat

 9. ticket:10 ``signals`` Create signal processor that, for every model, creates the db entry about the object creation/editing/deletion
 10. ticket:13 ``understanding`` Your customer sends the change request. Task: understand what he needs and implement.

  Customer's text:

   ``About requests log: we have to add a priortiy field,
   so we can show the different requests in the order we want.
   Priority 1 (or = 0) will be the standard selection.``

  Task: understand what he needs and implement.

 .. _`django widget`: http://docs.djangoproject.com/en/dev/ref/forms/widgets/
