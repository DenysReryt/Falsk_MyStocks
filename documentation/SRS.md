# **My Stocks**

## Vision

"My Stocks" is a web-application that allows users to access and record the information about stocks and also about
users.

Application should provide:

+ Storing valid stocks, users in a database;
+ Display list of stocks;
+ Updating the list of stocks (adding, editing, removing);
+ Display list of users;
+ Updating the list of users (adding, editing, removing);
+ Display the number of stocks for each user;
+ Display list of users for selected company who own its stocks;
+ Display list of stocks for selected user;
+ Updating list of stocks for selected user (adding, editing, removing);
+ Filtering by price for stocks;
+ Filtering by sum for list of stocks for selected user;
+ Filtering by registration date for users.

**Home page:**

Page contains a greeting and selection of a section from the list of stocks to the list of users.

![Home page](https://www.linkpicture.com/q/1_379.png)

Pic. 1 View of the home page

## 1. Stocks

### 1.1 Display list of stocks

The mode is designed to view the list of stocks, if it is possible to display the stocks sorted by the price.

***Main scenario:***

+ User select item "List of stocks";
+ Application displays list of all stocks.

![List of stocks](https://www.linkpicture.com/q/1_888.png)

Pic. 1.1 View the stock list

The list displays the following columns:

+ Code - unique auction code;
+ Company - the company to which the stocks belong;
+ Sector - the industry in which the company operates;
+ Amount - the number of all stocks of a given company;
+ Price ($) - price for the one stock;

***Filtering by price:***

+ In the stock list view mode, the user sets a price filter and presses the refresh list button (to the right of the
  price entry field);
+ The application will display a form to view the list of stocks with updated data.

Restrictions:

+ Start price of the stock should be less than end price of the stock;
+ If start price is blank, then filtering by end price only.
+ If end price is blank, then filtering by start price only.
+ Updating data after selecting the filtering conditions is carried out by pressing the "Refresh" button.

### 1.2 Add stock

***Main scenario:***

+ User clicks the “Add” button in the stock list view mode (at the top of stock table);
+ Application displays form to enter stock data;
+ User enters stock data and presses "Save" button;
+ If any data is entered incorrectly, incorrect data messages are displayed;
+ If entered data is valid, then record is adding to database;
+ If error occurs, then error message is displaying;
+ If new stock record is successfully added, then list of stocks with added records is displaying.

***Cancel operation scenario:***

+ User clicks the “Add” button in the stocks list view mode (at the top of stock table);
+ Application displays form to enter stock data;
+ User enters stock data and presses "Cancel" button;
+ Data don’t save in database, then list of stocks records is displaying to user.

![Add stock](https://www.linkpicture.com/q/1_1589.png)

Pic. 1.2 Add stock

When adding the stock, the following details are entered:

+ Company - the company to which the stocks belong;
+ Sector - the industry in which the company operates;
+ Amount - the number of all stocks of a given company;
+ Price ($) - price for the one stock;

Constraints for data validation:

+ Company – maximum length of 90 characters;
+ Sector – maximum length of 90 characters;
+ Amount – maximum length of 6 characters;
+ Price – maximum length of 6 characters.

### 1.3 Edit stock

***Main scenario:***

+ User clicks the “Edit” button in the stocks list view mode;
+ Application displays form to enter stock data;
+ User enters stock data and presses "Save" button;
+ If any data is entered incorrectly, incorrect data messages are displayed;
+ If entered data is valid, then edited data is added to database;
+ If error occurs, then error message is displaying;
+ If stock record is successfully edited, then list of stocks with added records is displaying.

***Cancel operation scenario:***

+ User clicks the “Edit” button in the stocks list view mode;
+ Application displays form to enter stock data;
+ User enters stock data and presses "Cancel" button;
+ Data don’t save in database, then list of stocks records is displaying to user.

![Edit stock](https://www.linkpicture.com/q/1_1590.png)

Pic. 1.3 Edit stock

When editing the stock, the following details are entered:

+ Company - the company to which the stocks belong;
+ Sector - the industry in which the company operates;
+ Amount - the number of all stocks of a given company;
+ Price ($) - price for the one stock;

Constraints for data validation:

+ Company – maximum length of 90 characters;
+ Sector – maximum length of 90 characters;
+ Amount – maximum length of 6 characters;
+ Price – maximum length of 6 characters.

### 1.4 Removing the stock

***Main scenario:***

+ The user, while in the list of stocks, presses the "Delete" button in the selected stock line;
+ If the stock can be removed, a confirmation dialog is displayed;
+ The user confirms the removal of the stock;
+ Record is deleted from database;
+ If error occurs, then error message displays;
+ If stock record is successfully deleted, then list of stocks without deleted records is displaying.

![Delete stock](https://www.linkpicture.com/q/1_889.png)

Pic. 1.4 Delete stock dialog

***Cancel operation scenario:***

+ The user, while in the list of stocks, presses the "Delete" button in the selected stock line;
+ Application displays confirmation dialog "Please confirm to delete stock";
+ User press "Cancel" button;
+ List of stocks without changes is displaying.

## 2. Users

### 2.1 Display list of users

This mode is intended for viewing and editing the users list.

***Main scenario:***

+ User selects item "List of Users";
+ Application displays list of users.

![List of Users](https://www.linkpicture.com/q/1_300.png)

Pic. 2.1 View of the user list

The list displays the following columns:

+ id - specific code for each user;
+ First name – user’s first name, you can click on and go to the page with the information about transactions 
  history for stocks;
+ Last name – user’s last name;
+ Stocks amount - number of stocks owned by this user;
+ Registration date – user’s date registration;
+ Phone – user’s phone number.

***Filtering by registration date:***

+ In the users list view mode, the user sets a registration date filter and presses the "Search" button (to the
  right of the registration date entry field);
+ The application will show the users only for a certain registration date of the selected period.

Restrictions:

+ Start registration date should be less than end registration date;
+ If start registration date is blank, then filtering by end registration date only.
+ If end registration date is blank, then filtering by start registration date only.
+ Updating data after selecting the filtering conditions is carried out by pressing the "Search" button.

### 2.2 Add user

***Main scenario:***

+ User clicks the "Add" button in the users list view mode;
+ Application displays form to enter user data;
+ User enters user’s data and presses "Save" button;
+ If any data is entered incorrectly, incorrect data messages are displayed;
+ If entered data is valid, then record is adding to database;
+ If error occurs, then error message is displaying;
+ If new user record is successfully added, then list of users with added records is displaying.

***Cancel operation scenario:***

+ User clicks the "Add" button in the users list view mode;
+ Application displays form to enter user’s data;
+ User enters user’s data and presses "Cancel" button;
+ Data don’t save in database, then list of users records is displaying to user.

![Add User](https://www.linkpicture.com/q/1_1592.png)

Pic. 2.2 Add user

When adding a user, the following details are entered:

+ First name – user’s first name;
+ Last name – user’s last name;
+ Phone – user’s phone number.

Constraints for data validation:

+ First name – maximum length of 45 characters;
+ Last name – maximum length of 45 characters;
+ Phone – unique, maximum length of 30 characters.

### 2.3 Edit user

***Main scenario:***

+ User clicks the "Edit" button in the users list view mode;
+ Application displays form to enter user data;
+ User enters user’s data and presses "Save" button;
+ If any data is entered incorrectly, incorrect data messages are displayed;
+ If entered data is valid, then edited data is added to database;
+ If error occurs, then error message is displaying;
+ If user’s record is successfully edited, then list of users with added records is displaying.

***Cancel operation scenario:***

+ User clicks the "Edit" button in the users list view mode;
+ Application displays form to enter user data;
+ User enters user data and presses "Cancel" button;
+ Data don’t save in database, then list of users records is displaying to user.

![Edit User](https://www.linkpicture.com/q/1_1593.png)

Pic. 2.3 Edit user

When editing the user information, the following details are entered:

+ First name – user’s first name;
+ Last name – user’s last name;
+ Phone – user’s phone number.

Constraints for data validation:

+ First name – maximum length of 45 characters;
+ Last name – maximum length of 45 characters;
+ Phone – unique, maximum length of 30 characters.

### 2.4 Removing user

***Main scenario:***

+ The user, while in the list of users mode, presses the "Delete" button in the selected user line;
+ Application displays confirmation dialog "Please confirm delete user";
+ The user confirms the removal of the user;
+ Record is deleted from database;
+ If error occurs, then error message displays;
+ If user record is successfully deleted, then list of users without deleted records is displaying.

***Cancel operation scenario:***

+ User is in display mode of users list and press "Delete" button;
+ Application displays confirmation dialog "Please confirm delete user";
+ User press "Cancel" button;
+ List of users without changes is displaying.

![Delete User](https://www.linkpicture.com/q/1_1595.png)

Pic. 2.4 Delete user dialog

## 3. Stocks for a selected user

### 3.1 Display list of stocks for selected user

This mode is intended for viewing and editing the stocks for selected user.

***Main scenario:***

+ User selects item "List of Users";
+ Then, user clicks on name of user;
+ Application displays list of stocks for selected user.

![List of Stocks for selected user](https://www.linkpicture.com/q/1_1612.png)

Pic. 3.1 View of the stock list for selected user

The list displays the following columns:

+ id - company id that sells stocks;
+ Company - the company to which the stocks belong;
+ Stocks amount - number of stocks owned by this user in particular company;
+ Sum - sum of stocks amount for each company.

***Filtering by sum:***

+ In the stock list for selected user view mode, the user sets a sum filter and presses the refresh list button (to the
  right of the sum entry field);
+ The application will show the stocks only for a certain sum of the selected range.

Restrictions:

+ Start sum should be less than end sum;
+ If start sum is blank, then filtering by end sum only.
+ If end sum is blank, then filtering by start sum only.
+ Updating data after selecting the filtering conditions is carried out by pressing the "Refresh" button.

### 3.2 Buy stocks

***Main scenario:***

+ User clicks the "Buy stocks" button in the stock list for selected user view mode;
+ Application displays form to enter stock data (Company, stocks amount - must be less than the total number of stocks
  sold by this company);
+ User enters stock data and presses "Save" button;
+ If any data is entered incorrectly, incorrect data messages are displayed;
+ If entered data is valid, then record is adding to database;
+ If error occurs, then error message is displaying;
+ If new stock record is successfully bought, then list of stocks for selected user with added records is displaying.

***Cancel operation scenario:***

+ User clicks the "Buy stocks" button in the stock list for selected user view mode;
+ Application displays form to enter stock data (Company, stocks amount - must be less than the total number of stocks
  sold by this company);
+ User enters stock data and presses "Cancel" button;
+ Data don’t save in database, then list of stocks for selected user records is displaying to user.

![Buy stocks](https://www.linkpicture.com/q/1_1599.png)

Pic. 3.2 Buy stocks

When buying a stocks, the following details are entered:

+ Company - the company to which the stocks belong;
+ Stocks amount - number of stocks in particular company to be purchased;

Constraints for data validation:

+ Company – maximum length of 45 characters;
+ Stocks amount – maximum length of 30 characters.

### 3.3 Sell stock

***Main scenario:***

+ User clicks the "Sell stock" button in the stock list for selected user view mode;
+ Application displays confirmation dialog "Please confirm to delete stock";
+ The user confirms the removal of the user;
+ Record is deleted from database;
+ If error occurs, then error message displays;
+ If stock record is successfully deleted, then list of users without deleted records is displaying.

***Cancel operation scenario:***

+ User clicks the "Sell stock" button in the stock list for selected user view mode;
+ User presses "Cancel" button;
+ Data don’t save in database, then the stock list for selected user records is displaying to user.

![Sell stock](https://www.linkpicture.com/q/1_1651.png)

Pic. 3.3 Sell stock


