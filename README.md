# Console CRM

Console CRM is a Python-based terminal application designed to manage customer relationships effectively. Integrated with the Google Sheets API, this tool offers essential CRM functions directly from the console, making it a versatile solution for businesses seeking a lightweight and accessible customer management system. The application is deployed on Heroku, ensuring it is always accessible and easy to use.

You can view and test the project [here](https://console-crm-23bb748056f0.herokuapp.com/)

![ConsoleCRM Mockup](documentation/mockup.png)

## Project Rationale
Console CRM was developed to address the need for an accessible, efficient, and user-friendly customer relationship management system. By integrating essential CRM functions with the power of Python and Google Sheets, Console CRM aims to streamline customer management processes for businesses of all sizes.

### Key Project Goals:
-   **Simplifying Customer Management:** Provide a straightforward platform for businesses to manage customer information without the complexity of larger CRM systems.
-   **Enhancing Data Accessibility:** Utilize Google Sheets for easy data access, updates, and collaboration.
-   **Automating Routine Tasks:** Reduce the manual effort required to manage customer data, improving overall efficiency and accuracy.

### Target Audience

Console CRM is designed for a diverse range of users who need a reliable CRM solution:

-   **Small to Mid-Sized Businesses:** Companies looking for a cost-effective CRM solution that is easy to implement and use.
-   **Sales and Marketing Teams:** Professionals who need to manage customer interactions and track communications efficiently.
-   **Freelancers and Consultants:** Individuals who require a simple yet effective way to maintain client relationships and streamline their workflows.

By addressing the needs of these groups, Console CRM aims to become a vital tool in managing customer relationships, improving productivity, and fostering business growth.

### User Stories

#### Demographics
**Name:** Sarah Lee  
**Age:** 35  
**Occupation:** Marketing Manager  
**Location:** New York, NY

#### Background
Sarah is a marketing manager who oversees a team responsible for client relationships and campaign management. She values tools that enhance productivity and streamline communication, especially those that help maintain accurate customer records.

#### Motivations and Goals
**Efficiency:** Sarah aims to improve her team’s efficiency in managing customer data.  
**Automation:** She looks for ways to automate repetitive tasks like sending emails and updating customer information.  
**Accessibility:** Sarah needs a CRM system that she and her team can access from anywhere.  
**Accuracy:** Maintaining up-to-date and precise customer records is crucial for Sarah.

#### How Sarah Uses the Console CRM
**Customer Overview:** Regularly reviews all customer data to stay updated.  
**Customer Search:** Uses the search function to quickly locate specific customer details.  
**Editing Records:** Updates customer information to ensure records are current.  
**Adding Customers:** Adds new customers to keep the database comprehensive.  
**Deleting Records:** Removes obsolete or incorrect customer information.  
**Email Communication:** Sends emails directly from the CRM to streamline communication.

#### Why Sarah Loves the Console CRM
**Efficient Management:** Provides an organized way to handle customer data.  
**Time-Saving:** Automation features reduce the time spent on routine tasks.  
**Convenient Access:** Can be accessed from anywhere via Heroku.  
**Reliable Data:** Ensures customer records are always accurate and up-to-date.

#### Detailed User Journey
**Phase 1: Discovery**  
**Trigger:** Sarah learns about Console CRM from an industry webinar.  
**Research:** Visits the GitHub repository, explores the README, and watches a demo.  
**Decision:** Decides to deploy the app on Heroku for a trial run.

**Phase 2: Onboarding**  
**Setup:** Clones the repository and configures the Google Sheets API connection.  
**Tutorial:** Follows the provided setup instructions to get started.

**Phase 3: Daily Use**  
**Customer Management:** Uses the console to view, add, edit, and delete customer records.  
**Email Sending:** Utilizes the email feature for direct communication with customers.

**Phase 4: Optimization**  
**Feedback Loop:** Continuously updates and refines customer data based on team feedback.  
**Customization:** Adjusts CRM settings to better fit her team’s workflow.

**Phase 5: Advocacy**  
**Loyal User:** Becomes a regular user, appreciating the CRM’s efficiency and reliability.  
**Advocate:** Recommends Console CRM to other managers and industry peers.

#### User Benefits
**Streamlined Customer Management:**
- Efficiently manage customer data with intuitive console commands.

**Automation:**
- Automate routine tasks like sending emails and updating records.

**Accessibility:**
- Access customer data from anywhere using the Heroku platform.

**Real-Time Updates:**
- Ensure customer data is always current and accurate.

**User-friendly Experience:**
- Enjoy a smooth and intuitive interface designed for ease of use.
- Quickly get started with clear instructions and helpful prompts.

**Motivation and Rewards:**
- Experience the satisfaction of maintaining a well-organized customer database.
- Strive for efficient data management and seamless communication.

**Accessibility:**
- Access the CRM from various devices with internet connectivity.
- Easily manage customer data anytime, anywhere.

## Features

Console CRM offers a comprehensive set of features designed to streamline customer relationship management through an intuitive and efficient console-based interface. Here’s a breakdown of the key functionalities:

### Customer Management
![Main Menu](documentation/screenshots/main-menu-screenshot.PNG)
-   **Add New Customers:** Easily add new customer records to the database, including essential contact information and notes.
-   **Edit Existing Customers:** Update customer details with new information to keep records current and accurate.
-   **Delete Customers:** Remove obsolete or incorrect customer entries to maintain a clean and relevant database.
-   **Search Customers:** Quickly locate customer records using powerful search functionality to find specific details swiftly.

### Data Integration and Accessibility
![List of customers](documentation/screenshots/show-customers-screenshot.PNG)
-   **Google Sheets Integration:** Seamlessly sync customer data with Google Sheets, ensuring easy access, updates, and collaboration.
-   **Real-Time Updates:** Perform customer operations with instantaneous updates, ensuring all users see the latest information without delay.
-   **Heroku Deployment:** Access the CRM from anywhere with an internet connection, thanks to its deployment on Heroku.

### Automation and Efficiency
![Email sending](documentation/screenshots/email-screenshot.PNG)
-   **Automated Email Communication:** Send emails directly from the CRM, automating routine communication tasks and saving time.
-   **Data Validation:** Ensure data accuracy with built-in validation checks that prevent errors and inconsistencies.

### User-Friendly Interface

-   **Rich Text Formatting:** Utilize the `rich` library to enhance the console interface with colorful and styled text outputs for better readability.
-   **Intuitive Commands:** Access all CRM functionalities through simple and clear console commands, making it easy to navigate and use.

### Future Features

Console CRM is continuously evolving to enhance user experience and functionality. Here are planned future features:

-   **Mass Email Communication:** Enable sending emails to all customers or specific groups directly from the CRM.
    
-   **Customer Groups:** Implement the ability to categorize customers into groups for better organization and targeted communication.
    
-   **Batch Customer Deletion:** Allow deletion of multiple customers at once to streamline database maintenance.
    
-   **Communication History:** Provide a log of communications with customers, including emails and other interactions.
    
-   **Bulk Customer Upload/Import:** Enable the upload, addition, or import of multiple customers simultaneously to expedite database population and updates.
    
These features are designed to further streamline customer relationship management, enhance productivity, and provide additional flexibility in managing customer interactions and data.

## Flowcharts

**main_menu:**
```mermaid
graph TD;
    Start[Start] --> Initialize[Initialize ConsoleCRM];
    Initialize --> ConnectDB[Connect to Database];
    ConnectDB --> DisplayMenu[Display Main Menu];
    DisplayMenu --> UserInput{User Input};
    UserInput -- Choice 1 --> ShowAll[Show all customers];
    UserInput -- Choice 2 --> Search[Search customer];
    UserInput -- Choice 3 --> Edit[Edit customer];
    UserInput -- Choice 4 --> Add[Add new customer];
    UserInput -- Choice 5 --> Delete[Delete customer];
    UserInput -- Choice 6 --> SendEmail[Send an email];
    UserInput -- Choice 7 --> Exit[Exit Program];
    ShowAll --> DisplayMenu;
    Search --> DisplayMenu;
    Edit --> DisplayMenu;
    Add --> DisplayMenu;
    Delete --> DisplayMenu;
    SendEmail --> DisplayMenu;
    Exit --> End[End];
```

**show_all_customers:**
```mermaid
graph TD;
    A[Start] --> B(Show All Customers)
    B --> C{Customers Found?}
    C -- Yes --> D[Display Customers]
    C -- No --> E[Display Message: No customers found.]
    D --> F(Return to Main Menu)
    E --> F(Return to Main Menu)
    F --> G[End]
```

**search_customer:**
```mermaid
graph TD;
    A[Start] --> B(Search Customer)
    B --> C{Customers Found?}
    C -- Yes --> D[Display Search Results]
    C -- No --> E[Display Message: No matching customers found.]
    D --> F[Return to Main Menu]
    E --> F[Return to Main Menu]
    F --> G[End]
```

**edit_customer:**
```mermaid
graph TD;
    Start --> A;
    A[Search Query Input] --> B;
    B{Valid} -->|Yes| C[Search Customers];
    B -->|No| O[Display Error Message];
    C{Results Found} -->|Yes| D[Display Search Results];
    C -->|No| P[Display No Results Message];
    D --> E[Select Customer ID to Edit];
    E --> F{Field to Edit or Save};
    F -->|Save| G[Save Changes];
    G --> H[Display Success Message];
    H --> I[Return to Main Menu];
    F -->|Field| J[Edit Field Value];
    J --> K{Validation};
    K -->|Valid| L[Update Field];
    L --> M[Display Success Message];
    K -->|Invalid| N[Display Error Message];
    N --> J;
    P --> Q[Return to Main Menu];
```

**add_new_customer:**
```mermaid
graph TD;
    A[Start] --> B(Add New Customer)
    B --> C{Input Customer Details}
    C --> D{Validation}
    D -- Valid --> E[Save Customer]
    D -- Invalid --> F[Display Error Message]
    E --> G[Customer Added Successfully]
    F --> C
    G --> H[Return to Main Menu]
    H --> I[End]
```

**delete_customer:**
```mermaid
graph TD;
    A[Start] --> B(Delete Customer)
    B --> C{Search for Customer}
    C --> D{Customer Found?}
    D -- Yes --> E(Confirm Deletion)
    E --> F{Confirmation: Yes/No}
    F -- Yes --> G[Delete Customer]
    F -- No --> B(Re-enter ID)
    D -- No --> H[Display Message: No matching customers found.]
    G --> I[Customer Deleted Successfully]
    H --> A(Return to Main Menu)
    I --> J[End]
```

**send_customer_email:**
```mermaid
graph TD;
    A[Start] --> B(Send Customer Email)
    B --> C{Search for Customer}
    C --> D{Customer Found?}
    D -- Yes --> E(Select Customer)
    E --> F{Input Email Details}
    F --> G[Send Email]
    G --> H[Email Sent Successfully]
    D -- No --> I[Display Message: No matching customers found.]
    H --> J[Return to Main Menu]
    I --> A(Return to Main Menu)
    J --> K[End]
```

## Technologies Used

**Python:**  
Employed for backend logic, managing customer data, and interacting with APIs.

**Google Sheets API:**  
Used for storing, updating, and retrieving customer data efficiently.

**DataManager, Validator, MailManager:**  
Custom modules for handling data management, validation, and email operations.

**Heroku:**  
Platform for deploying the application, ensuring accessibility from any location.

**StackEdit:**  
Markdown editor used to create and format the README.md file.

**TAAG (Text to ASCII Art Generator):**  
Utilized for generating the ASCII logo for the application, available at [TAAG](https://patorjk.com/software/taag/).

### Data Storage
The Console CRM app employs Google Sheets for effective data storage and management. Here’s how the data is organized and utilized within the app:

**Customer Data:**
A worksheet named `contacts` contains all customer details, including names, contact information, and other relevant data. This organization ensures easy access and management of customer records.  

![Contacts Spreadsheet](documentation/screenshots/contacts-spreadsheet.PNG)

**Customer Operations:**
Each customer operation (add, edit, delete) is reflected in the `contacts` worksheet, ensuring that all changes are tracked and up-to-date.

### Data Management and Privacy Protection

**Seamless Google Sheets Integration:** Console CRM leverages the `gspread` library to provide seamless integration with Google Sheets, enabling users to manage customer data effectively. Authentication is managed using a service account, with credentials securely stored in a `creds.json` file. This file is purposefully kept out of the version control repository to ensure the highest level of security.

**Robust Data Privacy:** Ensuring data privacy is a cornerstone of Console CRM. All sensitive information, including service account details and API keys, are securely stored and kept confidential. This strategy protects user data from unauthorized access and ensures that the application maintains its integrity and trustworthiness.

**Dynamic Real-Time Updates:** Console CRM is designed to update customer data in real-time. As soon as any operation is performed, users can immediately see the most current information. This feature is essential for maintaining accurate and up-to-date records, ensuring that all users have access to the latest customer data without delay.

**Enhanced Security Protocols:** Access to the Google Sheets API is managed through OAuth2, which uses restricted scopes to limit access to only the necessary operations. This method enhances the security of data interactions within the app by minimizing exposure to potential security risks. By strictly controlling API permissions, Console CRM ensures that data exchanges are secure and confidential.


### Python Libraries Used
The Console CRM application relies on the following Python libraries for its functionality:

**time:**  
Provides functions for manipulating and formatting time-related data.

**json:**  
Enables parsing and generation of JSON data, facilitating data interchange.

**re:**  
Supports advanced string manipulation and regular expression operations.

**rich:**  
Enhances the user interface with rich text formatting, adding color and style to terminal outputs.

**smtplib, MIMEText, MIMEMultipart:**  
Enable email functionalities, allowing the application to send emails directly.

**DataManager (Custom Module):**  
Handles data management tasks within the application.

**Validator (Custom Module):**  
Performs data validation, utilizing `@staticmethod` for utility methods that don't require class instances.

**MailManager (Custom Module):**  
Manages email operations, integrating with the `smtplib` library.

**google-auth:**  
Manages authentication to Google APIs, securing access to Google Sheets.

**google-auth-oauthlib:**  
Facilitates OAuth 2.0 authentication flows for accessing Google Sheets.

**gspread:**  
Allows interaction with Google Sheets, used for storing and updating customer data.

These libraries and modules are essential for the application’s core functionalities and are listed in the `requirements.txt` file for easy installation using `pip`.

## Testing

### PEP8 Validation

I validated the code using the CI Python Linter [PEP8 CI Linter](https://pep8ci.herokuapp.com/#), ensuring that the code met PEP8 guidelines.

-   **run.py:**  
    ![run.py testing](documentation/screenshots/run-test.PNG)
-   **data_manager.py:**  
    ![run.py testing](documentation/screenshots/data-test.PNG)
-   **validator.py:**  
    ![run.py testing](documentation/screenshots/validator-test.PNG)
-   **mail_manager.py:**  
    ![run.py testing](documentation/screenshots/mail-test.PNG)

### Manual Testing

I performed the following tests. All passed with expected results.

-   **Validation of Customer Data Input:**
    -   Tested for string inputs, negative numbers, special characters
-   **Search Functionality:**
    -   Verified searching for existing and non-existing customers
-   **Edit Customer Data:**
    -   Ensured data updates correctly and displays the updated information
-   **Add New Customer:**
    -   Confirmed new customer is added correctly to the Google Sheets
-   **Delete Customer:**
    -   Verified the customer is removed from the Google Sheets
-   **Send Email:**
    -   Tested email sending functionality, ensuring emails are sent and received
-   **API Error Handling:**
    -   Simulated connectivity issues and checked for graceful error handling without crashing
-   **User Interface:**
    -   Confirmed that all terminal outputs are clear, color-coded appropriately using `Colorama`

### Peer Review

I shared the application with peers, colleagues, and friends, requesting their feedback and insights. They tested various features and provided valuable input on usability and functionality.

### Bugs

-   **Rich library not added to requirements:**  
    Manually added due to compatibility issues with pip during installation.
    
-   **MailManager crashing due to UTF-8 encoding errors (unable to handle ä, ü, and ö):**  
    Fixed by incorporating the `email.mime` library to handle character encoding properly.
    
-   **First search results not displaying when searching customers:**  
    Resolved by removing `[1:]` to ensure all search results are correctly displayed.
    
-   **Main menu crashing on incorrect input:**  
    Implemented a while loop to prompt for valid input until a correct choice is made, preventing crashes.


## Deployment

### Set Up the Google Sheet

1.  **Sign in to your Google Account:**
    
    -   Make sure you're signed in with your personal Google account.
2.  **Create a Google Sheets file:**
    
    -   Navigate to Google Sheets (sheets.google.com) and click on the "+ Blank" button to create a new spreadsheet.
3.  **Navigate to the Google API Library:**
    
    -   Go to the Google API Library (console.developers.google.com).
4.  **Create a new project:**
    
    -   Click on the dropdown on the navbar to create a new project.
5.  **Enable Google Sheets API:**
    
    -   Search for the "Google Sheets API" and enable it. This can take up to 10 seconds.
6.  **Create Credentials:**
    
    -   In the "APIs and services" navbar on the left, go to the "Credentials tab". Click on "+ CREATE CREDENTIALS" and select "Service Account".
7.  **Provide Service Account Details:**
    
    -   In the first step (service account details), provide a name for the service account, e.g., "guess-weather-service" and click on "Create and continue".
8.  **Grant Service Account Access:**
    
    -   In the second step, grant the service account access to the project. You can select a role from the dropdown menu, such as "Project" > "Editor". Click on "Continue".
9.  **Generate Key:**
    
    -   In the third step, click on "+ CREATE KEY" button. Select "JSON" as the key type, and click "Create". This will trigger the download of a JSON file which contains your service account credentials.
10.  **Secure JSON file:**
    
	   -   Save this file in a safe folder for further use. This file can be downloaded only once!
11.  **Share the Google Sheets file with your Service Account:**
    
	   - In order for your service account to access your Google Sheets file, you need to share the file with it. You can do this by going to your Google Sheets file, clicking on the "Share" button in the top right corner above the worksheet, and entering the email address of your service account (you can find this in the JSON file you downloaded earlier).

### Create Repositories

1.  **Register GitHub account if you don't have one.**
    
2.  **Go to My GitHub page.**
    
3.  **Fork the Repository:**
    
    -   Click on the "Fork" button at the top right corner of the page. This will create a copy of the repository in your GitHub account.
4.  **Clone the Forked Repository:**
    
    -   Navigate to your forked repository on GitHub. Click on the "Code" button and copy the URL provided under "Clone with HTTPS" or "Clone with SSH" depending on your preference.
5.  **Clone the Repository Locally:**
    
    -   Open your terminal or command prompt. Change the current working directory to the location where you want the cloned directory. Type `git clone`, and then paste the URL you copied earlier. For example:
        `git clone https://github.com/p-harting/console-crm.git` 
        
    -   Press Enter to create your local clone.
6.  **Make Changes Locally and stage and Push them to your remote repository as needed.**
    
7.  **Include your creds.json file in .gitignore:**
    
    -   Ensure your `creds.json` file is added to the `.gitignore` file to avoid pushing it to a public repository like GitHub.

### Install Python Libraries

1.  **Install necessary Python libraries using requirements.txt:**
    -   run the following command in your Python environment to install the libraries:
        `pip install -r requirements.txt` 
        

### Set up Python Client

1.  **Copy the JSON key file:**
    
    -   COPY the JSON key file you saved as per the instructions above to your project root directory.
2.  **Rename the file to creds.json:**
    
    -   IMPORTANT! Rename this file exactly `creds.json`.
   
### Deployment to Heroku

1.  **Set dependencies:**
    
    -   Run the following command in the terminal to set up project dependencies:
        `pip3 freeze > requirements.txt`
    -   Additionally, you will need to manually add the `rich` library to your project dependencies, as it does not appear in the list generated by `pip freeze`. For more details, refer to the bugs section.
        
2.  **Create a Heroku account if you don't have one.**
    
3.  **Login and create a new app:**
    
    -   Name your app, choose region, and hit 'Create app'.
4.  **Set Config Vars:**
    
    -   Go to the app settings page on Heroku, and in the Config Vars section:
        -   Add `CREDS` with the value of your `creds.json` contents.
        -   Add `PORT` with the value `8000`.
5.  **Set Buildpacks:**
    
    -   Add Python and Node.js buildpacks in the buildpacks section.
6.  **Deploy from GitHub:**
    
    -   Connect your GitHub repository to Heroku.
    -   Enable automatic deploys if desired.
    -   Click "Deploy Branch" to deploy the app.

## Credits

This project was developed as part of my coursework at Code Institute, where I have gained substantial experience in Python programming. The knowledge and skills acquired during my studies have been crucial in the successful implementation of Console CRM.

- The ASCII text generator used for the logo was sourced from [TAAG](https://patorjk.com/software/taag/#p=display&f=Big&t=ConsoleCRM).
- Techniques on how and why to use `@staticmethod` were referenced from [Stack Overflow](https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python).
- Regex for email validation was inspired by the guide provided by [ZeroBounce](https://www.zerobounce.net/python-email-verification/).
- The tutorial on sending emails in Python was followed from a [YouTube video](https://www.youtube.com/watch?v=ueqZ7RL8zxM).