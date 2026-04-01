# PHPTravels

## Website URL

<https://phptravels.com/demo>

## Navigation

PHP Travels is a travel booking platform. Users land on the home page with a top navigation bar (Home, Hotels, Flights, Tours, Cars, Visa, Offers, Blog) and a search widget with tabs for Hotels, Flights, Tours, and Cars. The header also includes currency and language selectors plus Login / Signup; after authentication, the user dropdown provides access to the dashboard and account management.

## Functional Description

### 1. Home Page And Search

The home page features a search widget with tabs for Hotels, Flights, Tours, and Cars; selecting a tab switches the visible fields for that service type. The Search action validates required fields for the active tab and, when valid, redirects to the corresponding results listing page.

### 2. Registration

Registration is available via Signup in the top navigation (or from the login page) and collects user details including name, email, password/confirm password, mobile number (with country code), and a required terms-and-conditions checkbox. Submission validates required fields, password match, valid email format, and email uniqueness before creating the account and granting access.

### 3. Login

Login uses an email and password form (optionally with "Remember Me"), with access to Forgot Password and a registration link for new users; social login may be available if enabled. Successful authentication redirects to the account dashboard (or the originally-requested protected page); failures show an error and may require CAPTCHA after repeated attempts.

### 4. Forgot Password

Forgot Password allows users to request a reset link by entering their registered email address; when found, the system sends a reset link that expires after 24 hours. Users set and confirm a new password via the link and return to the login page with success feedback; unknown emails return an error.

### 5. Hotels Search And Listing

Hotels search is available from the home page (Hotels tab) and the Hotels navigation link and includes destination/hotel input, date pickers, room count, and guest selectors. Successful searches lead to a hotels listing with hotel cards and common controls such as filters, sorting, and pagination.

### 6. Hotel Details And Booking

Hotel details include property information such as images, description, map, amenities, room availability, reviews, and policies. Booking flows from selecting a room into a guest-details form with a price breakdown and proceeds to payment, requiring login for unauthenticated users.

### 7. Flights Search And Booking

Flights search supports trip type, origin/destination, dates, passenger counts, and cabin class; valid searches lead to a results list with flight details, filters, and sorting. Booking collects traveler and contact information (including passport details where required) and advances through validation to the payment step.

### 8. Tours Search And Booking

Tours search includes destination and date selection with additional controls such as tour type, duration, and budget, leading to a listing with tour cards and filters. Selecting a tour opens details (itinerary, inclusions/exclusions, availability, pricing) and proceeds through booking and payment, requiring login where applicable.

### 9. Cars Search And Booking

Cars search captures pick-up/drop-off locations, date/time, and driver age, and returns a listing grouped by vehicle category with common filters. Booking captures driver details, optional add-ons and insurance, and proceeds to payment with validation.

### 10. Visa Services

Visa services allow users to select nationality and destination country to view visa requirements, fees, and processing information. Users can submit a visa application with personal details, travel information, and required document uploads, and track application status from their account.

### 11. User Dashboard And Booking Management

After login, the dashboard provides access to account information and booking activity (for example, bookings, profile, wallet/credits, wishlist, reviews, settings, and logout). From My Bookings, users can view booking details and manage bookings via supported modification and cancellation flows with policy-based validation and notification.

### 12. Payment Processing

Payment pages show a full booking summary and total amount due and support common methods such as card payments, PayPal, bank transfer, and wallet/credits (if available). Successful payment produces a booking confirmation and email notification; failures display an error and allow retry.

### 13. Currency And Language Selection

Currency and language selectors in the header update prices and UI language across the site. Preferences may persist via user profile for authenticated users or via session/cookies for unauthenticated users.

### 14. Search And Filters

Listing pages provide sidebar filters and sorting controls that update results as users refine criteria. Active filters can be removed individually and can be cleared using a reset control.

### 15. Reviews And Ratings

Hotels, tours, and cars display aggregate ratings and review counts in listings, and show detailed reviews on item pages. Authenticated users who complete bookings can submit reviews with star ratings and written feedback.

### 16. Offers And Deals

The Offers section lists promotional deals with details such as discount/validity and provides a path into the booking flow. Offers can be filtered and may apply promotional codes automatically or via redirected searches.

### 17. Logout

Logout is available from the user menu and the dashboard, ends the current session, and redirects to the home page. After logout, protected pages redirect back to login.
