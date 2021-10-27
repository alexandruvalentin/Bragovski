## Encountered Issues

1. SERVER ERROR (500):
    - Causation: deleting an item from the database while having it in the shopping bag
    - >:heavy_check_mark: fixed according to the Slack Community
2. NoReverseMatch at /XYZ/XYZ
    - Causation: sending the wrong id's through POST forms
    - >:heavy_check_mark: fixed by calling the id's accordingly
3. Although there were numerous issues and bugs reported in the front-end, they didn't require a great amount of time to fix.

  
## Testing User Stories
  - ## As a shopper I want:
    - to view a list of products/services so that I can select and purchase
    >:heavy_check_mark: The products pages displays all available products
    - to view individual product/service details in order to decide what I like and suit my budget best
    >:heavy_check_mark: Product detail page displays all details about a specific product
    -  to quickly identify and access products so that I can learn more about what I want
    >:heavy_check_mark: The products page is accessible either from the menu or from the home page CTA
    - to easily view the total of my purchase at any time so that I can avoid going over budget
    >:heavy_check_mark: Clicking on the bag icon will take the user to their shopping bag where they can see all the contents in their bag
    - to feel that my personal details are secure so that I can confidently provide them to make a purchase
    >:heavy_check_mark: Stripe webhooks have been set up to keep the transactions secure
    - view an order confirmation after checkout so that I can double-check for any mistakes
    >:heavy_check_mark: An order details page will be displayed to the user after the purchase
    - to receive an email of confirmation after checkout so that I can keep a confirmation of what I've just ordered for my records
    >:heavy_check_mark: A confirmation email is sent with every succesful purchase straight to the user's inbox
    - to look up testimonials from other people that have worked with the artist so that I can possibly book a studio session in the future
    >:heavy_check_mark: All submitted testimonials are displayed for everyone on the Testimonials page
    - to be able to add testimonials to the section in order to share the experience I had working with the artist
    >:heavy_check_mark: On the testimonials page logged users can add reviews and later edit them from their profile page

    - ## As a website user I want:
    - to easily register for an account so that I can save my personal/delivery information
    >:heavy_check_mark: Users can register for an accout from the navigation menu profile icon
    - to easily log in and out so that I can quickly access my personal account information
    >:heavy_check_mark: Users can log in/out from their profile page.
    - to easily recover my password in case I forget it so that I can quickly recover access to my account
    >:heavy_check_mark: Users are able to reset their passwords endlessly.
    - to receive a confirmation email after registration so that I can verify that it was successful
    >:heavy_check_mark: Users will have to access the link sent to their inbox in order to gain access to the account portal
    - to be able to update my user profile information so that I can easily change delivery address, contact name or card details
    >:heavy_check_mark: Users can update their profile from the profile page

    - ## As a site admin I want:
    - to be able to add new products so that I can keep present the new products available
    >:heavy_check_mark: Admin users can add products from the Product Management section in the profile menu
    - to be able to update/remove products so that I can change/delete product criteria
    >:heavy_check_mark: Admin users can also update/remove any product available on the website
    - to be able to give admin rights so that I can allow other users to administer the website when necessary
    >:heavy_check_mark: Admin users can give admin rights to whomever they prefer


## Testing Functionality
  - ### Testing Links and Buttons
    - top navigation bar is fully functional, including the brand logo. :heavy_check_mark:
    - mobile navigation toggle "burger" is functional, opening and closing as expected. :heavy_check_mark:
    - all menu buttons link to the specific pages. :heavy_check_mark:
    - 'Add', 'Edit' and 'Delete' buttons act accordinly across the website. :heavy_check_mark:
    - sign up functionality sends a confirmation email to the user as expected

  - ### Testing Form Validation
    - Every form was tested for validation by trying to submit without data and then with one field at a time. Every field asked for input. :heavy_check_mark:

  - ### Testing CRUD Functionality
    - **CREATE**: The 'create' functionality was tested by adding data to the designated fields. Works as expected. Forms are being uploaded to the database correctly :heavy_check_mark:
    - **READ**: The 'read' functionality was tested by verifying that the generated data is being correctly displayed in the right section. :heavy_check_mark:
    - **UPDATE**: The 'update' functionality was tested all throughout the website. No issues found :heavy_check_mark:
    - **DELETE**: The 'delete' functionality was tested all throughout the website. Clicking on the Delete button will remove items accordingly. :heavy_check_mark:

## Testing Compatibility
  - ### Responsiveness :heavy_check_mark:
    - Responsiveness was explored and tested using DevTools and on a wide variety of devices of different sizes, in both portrait and landscape, in order to detect any issue. No issues were found; elements align correctly in space, none being obstructed. In conclusion, the website is fully responsive.

  - ### OS Test :heavy_check_mark:
    - Desktop
    > Testing was done on Windows 7 and Windows 10. Features appear to be functional from top to bottom. Buttons, links, slider and forms are all working correctly. No overflow, overlay or error messages encountered. In conclusion, the website is desktop system-cross compatible.
    - Mobile
    > Testing was done on Android 10, iOS 13 and iOS 14. Features appear to be functional from top to bottom. Buttons, links, slideshow gallery and contact form, all work correctly. No overflow, overlay or error messages encountered. In conclusion, the website is mobile system-cross compatible.

  - ### Devices test :heavy_check_mark:
    > Testing was done on ASUS TUF FX705G, Galaxy S20, iPhone 7/8/11/12/12 Pro and iPad Pro 12.9 2020. Features appear to be functional from top to bottom. Buttons, links, slider and forms are all working correctly. No overflow, overlay or error messages encountered. Everything falls into place in space. In conclusion, the website is platform-cross compatible.

  - ### Browser test :heavy_check_mark:
    > The website was tested on Google Chrome, Firefox, Safari and Microsoft Edge. Browser versions were all up to date. Further testing was done using [BrowserLing](https://www.browserling.com/). Features appear to be functional from top to bottom. Buttons, links, slider and forms are all working correctly. No overflow, overlay or error messages encountered. Everything falls into place in space. In conclusion, the website is browser-cross compatible.

## Testing Performance

The app's erformance was tested using Google Chrome's **Lighthouse** for both desktop and mobile. Extra mobile tests were made using an actual mobile device.

>   ![LightHouse Performance Result](https://github.com/alexandruvalentin/Bragovski/blob/main/docs/performance.png])  

## Testing Accessibility

The website's accessibility was tested using the [a11y Color Contrast Accessibility Validator](https://color.a11y.com/Contrast/).
> :heavy_check_mark: All Pages: The problems detected are concerning the footer elements contrast due which can be ignored.


## Code Validation
  - ### HTML :heavy_check_mark:
    > Tested and validated using W3C Validator. No errors to show.

  - ### CSS :heavy_check_mark:
    > Tested and validated with W3C CSS Validator. Only errors displayed are warnings which can be ignored.

  - ### JavaScript :heavy_check_mark:
    > Javascript methods and functions were tested for the expected outcome in the console using the console.log() command and the code was validated with [JSHint](https://jshint.com/).

  - ### Python :heavy_check_mark:
    > Python has been validated during the coding process using **[Pylint](https://www.pylint.org/)**. **No errors or issues**.

## Further Testing
  - ### Overflow :heavy_check_mark:
    > Every page was tested for overflow by using the [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln?hl=en-GB) chrome extension to highlight the elements margins. **No issues found**.

  - ### Spelling :heavy_check_mark:
    > English grammar & spelling throughout the website was checked using [LanguageTool](https://languagetool.org/#plugins) chrome extension.

  - ### Mobile Friendly :heavy_check_mark:
    > According to [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly?id=Azf0gym8vu8mKzd1bWgdIw), the app is mobile-friendly.


## Future testing 

- Automated testing
- Accessibility and performance