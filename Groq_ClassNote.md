



Title: Lecture Notes on Architecture Design and Documentation

I. Introduction

* Today's lecture focuses on one of the ways to create architectures and the best way to go through it
* Review of modeling and architecting, styles, patterns, and web architecture documentation

II. Assignments and Calendar

* One assignment is fully graded, another is in progress
* Follow the calendar for due dates, not the order of course assignments
* Some assignments may be out of order to give time to catch up or work on the overall course assignment

III. Architecture Decision Records (ADRs)

* ADRs should be effective in communicating and make sense in the context of the overall architecture
* ADRs should be connected to the architecture being documented and presented
* Example of an ADR: comparing Kubernetes and Lambdas, choosing Lambdas due to no cold start issues, and providing the logic behind the decision
* ADRs should not be too high-level; including diagrams and documentation can help
* Designing and implementing a proof of concept (POC) can help in making a decision

IV. Performance as a Concern in ADRs

* Performance can be a concern in ADRs
* Implementing a POC can help in deciding which technique is faster

V. Benefits of Following the Calendar

* Following the calendar can help students stay on track and avoid working on the wrong assignment
* Staying ahead of the game is possible since most of the covered material will be part of the deliverable due for the course

VI. Importance of ADRs in Architecture Documentation

* ADRs should not be random; they should be connected to the architecture being documented
* Documenting an architecture requires going through the decision-making process before sharing it with stakeholders.



Web Architectures Study Notes:

Introduction:
The lecture focuses on the evolution of web architectures, their documentation, and the clarity of their purpose. The discussion is not meant to delve into the technical details of each architecture but to evaluate their effectiveness and the way they have been documented and presented.

Key Points:

1. The foundation of web architectures was laid by TCP/IP in the 1960s, which evolved into the modern internet.
2. Web 1.0 started with the introduction of the World Wide Web by Tim Berners-Lee in the late 1980s and early 1990s.
3. Web 2.0, where we currently stand, is characterized by social media, high-speed communications, and advanced multimedia content.
4. Web 3.0, also known as the semantic web, is still emerging, with examples seen in blockchain, AI, VR, and AR technologies.

Timeline and Progression:

- The 1960s saw the inception of TCP/IP, which formed the basis of network computers and the internet.
- Web 1.0 began in 1989-1990 with Tim Berners-Lee's proposal, with the first websites and HTTP protocols being utilized in the mid-1990s.
- Web 2.0 started to catch fire around 1999-2000, characterized by dynamic web pages, social media, and high-speed communications.
- Web 3.0, or the semantic web, is still evolving, with examples seen in blockchain, AI, VR, and AR technologies. However, it takes time for standards to be adopted and agreed upon by different entities.

Web Architecture Components:

- Web browser: Makes a request to a web server.
- Web server: Receives the request and processes it.
- File system: Stores the files and data requested by the web browser.
- Database: Manages and stores data for dynamic web pages.
- Servlets: Small Java programs that run on web servers to dynamically generate content.

The evolution of web architectures has been marked by significant advancements since the 1960s, with the progression from Web 1.0 to Web 2.0 and now Web 3.0. Each stage has brought new features, capabilities, and ways of interacting with content. Understanding this evolution and the components of web architectures is essential for students in this course.



Study Notes:

I. Introduction to Web Architecture

* Static web pages: Request and response, no dynamic content or user interaction.
* Common Gateway Interface (CGI): Allows scripts to run on web servers, evolving into mechanisms like React and web frameworks.

II. Common Gateway Interface (CGI)

* CGI scripts facilitate communication between the web server and backend.
* CGI evolved into Java servlets, PHP, and various web frameworks (e.g., Angular, Ruby on Rails).

III. JavaScript and Client-Side Processing

* JavaScript runs on the web browser, enabling dynamic web pages and workload sharing between the client and server.
* Modern web architecture has evolved to include JavaScript engines on the client-side, reducing web server workload.

IV. Web Architecture Evolution

* In just four years, web architecture evolved from a simple browser-server model to a dynamic, multi-threaded system with model-view-controller (MVC) frameworks.
* The modern web architecture includes application servers, like Apache Tomcat, enabling complex logic and state management.

V. Multi-Threaded Architecture and Communication

* Modern web architecture allows for multi-threaded communication, with the ability to break down and document specific areas, such as application servers, databases, and web servers.
* The entire application lifecycle can be contained within the web app, allowing for better communication and management.

Key Concepts and Terms:

* Static web pages
* Dynamic web pages
* Request and response
* Common Gateway Interface (CGI)
* Web server
* Web frameworks (e.g., Angular, Ruby on Rails)
* JavaScript
* Client-side processing
* Model-view-controller (MVC) frameworks
* Multi-threaded architecture
* Application servers (e.g., Apache Tomcat)
* State management



Study Notes:

Subject: Evolution of Web Architecture and the Introduction of MVC and Flux Patterns

1. Introduction to MVC (Model-View-Controller) pattern:
   - The MVC pattern is a way to organize code in web applications.
   - The application server runs a controller, which receives actions from the view (web browser).
   - The controller then interacts with the model, which updates the view or refreshes it.
   - This modularization allows for larger applications with multiple models, controllers, and views.
   - Replacing HTML with markup files enhances the dynamicity and control of the application.

2. Challenges and improvements with MVC:
   - While MVC improves code modularization, it also introduces the challenge of managing configuration files that control how the code executes.
   - As applications become more complex, these configuration files become increasingly difficult to manage.

3. Web 1.0 and its evolution:
   - Web 1.0, which existed from 1995 to 2005, started with read-only content and evolved to support reasonable-sized applications with basic web architectures.
   - The introduction of the MVC pattern for web-centric application development was a significant improvement.

4. The shift to Web 2.0:
   - Starting in 2005-2006, the architecture shifted to Web 2.0, aiming to simplify the architecture by reducing the number of layers between the web server and the web application.
   - Web 2.0 enhancements allowed for running applications or parts of them on mobile devices or web browsers, with data and API calls happening in the back end.

5. The role of XMLHttpRequest and Xml in Web 2.0:
   - XMLHttpRequest and Xml were initially developed for Internet Explorer but were later adopted by Google for a different usage.
   - Google created JavaScript libraries compatible with Xml over Http, which led to the development of Gmail and Google Maps.
   - This shift enabled Web 2.0, allowing for the evolution of applications running on native operating systems like iOS or Android.

6. The impact of advancements in technology:
   - Many advancements in technology come from concepts that provide a step forward or an evolution from one set of components or architecture to a more advanced one.
   - In the case of Web 2.0, XML over Http and JavaScript libraries compatible with it were the enabling factors for this evolution.



Study Notes:

Title: Web Development - Ajax and Web 2.0

I. Introduction

* The lecture focuses on the transition from Web 1.0 to Web 2.0, with an emphasis on Ajax and its role in modern web development.

II. Ajax (Asynchronous JavaScript and XML)

* Ajax is an asynchronous JavaScript technique that allows for the updating of specific parts of a webpage without requiring a full page reload.
* Ajax achieves this by making background data requests, allowing for the creation of dynamic, interactive web applications.
* Ajax relies on the XMLHttpRequest (XHR) object, which enables the communication between the client and the server.
* Ajax allows for the separation of data, presentation, and logic, resulting in more efficient and user-friendly web applications.

III. Web 1.0 vs. Web 2.0

* Web 1.0 was characterized by static web pages with limited user interaction, while Web 2.0 introduced dynamic content and full-featured applications using web protocols.
* Web 2.0 supports multiple clients, including mobile apps and IoT devices, making it a significant evolution from Web 1.0.

IV. Ajax and Web 2.0

* Ajax played a crucial role in the development of Web 2.0, as it enabled the creation of more interactive and responsive web applications.
* Ajax facilitated the move away from static web pages, allowing for the development of Single Page Applications (SPAs) and other dynamic web solutions.
* Web 2.0 and Ajax have allowed for the creation of rich internet applications (RIAs) that provide a desktop-like user experience.

V. Ajax Architecture

* Ajax architecture involves the web browser making HTTP requests to a WebXML server responsible for backend processing and database access.
* The WebXML server returns HTML, JavaScript, style sheets, and the Ajax engine to the client.
* As the user interacts with the webpage, the Ajax engine makes requests, retrieves data, and updates the HTML page accordingly.

VI. Advantages of Ajax and Web 2.0

* Improved user experience through dynamic, interactive web applications
* Increased efficiency due to the separation of data, presentation, and logic
* Enhanced collaboration and social networking capabilities
* Support for multiple clients, including mobile and IoT devices

VII. Conclusion

* Ajax and Web 2.0 have revolutionized web development by enabling dynamic, interactive, and user-friendly web applications.
* The transition from Web 1.0 to Web 2.0, facilitated by Ajax, has led to the creation of rich internet applications and single-page architectures.
* Understanding Ajax and Web 2.0 concepts is essential for modern web developers, as they continue to shape the future of the web.



Study Notes:

Subject: Evolution of the World Wide Web - from Web 2.0 to Web 3.0

I. Introduction

* Web 3.0, the next generation of the World Wide Web, is emerging
* This note summarizes the evolution from Web 2.0 to Web 3.0, highlighting key components, architectural changes, and functionality improvements

II. Web 2.0 (2004-2005)

* Allows users to do useful things over the web
* Enabled by advancements such as HTTP/2 and MQTT protocols
* New components in the Web 2.0 architecture include:
	1. Content providers: Browser downloads application code from web servers or content delivery networks (CDNs)
	2. Content Delivery Networks (CDNs): Cache content for faster access, e.g., front-end running in a different region from the application
	3. Web application firewalls (WAF): Security measures to prevent denial-of-service attacks and control access to APIs
* Dynamic applications communicate with APIs using Ajax framework

III. Web 2.0 to Web 3.0 Transition

* Emergence of single-page applications (SPAs), such as Facebook and Twitter
* Personalization and dynamic content based on user interactions
* IoT devices and various communication protocols enable scalability
* Monetization drives ideas and development

IV. Semantic Web in Web 2.0

* Semantic Web concepts are being integrated into Web 2.0 architectures
* Personalization, dynamic content, and user interactions are becoming increasingly important

V. Web 3.0 (The Future)

* Anticipated features of Web 3.0 include:
	1. Decentralized and distributed web services
	2. Artificial intelligence and machine learning integration
	3. Improved data interoperability and sharing
	4. Enhanced privacy and security
* Web 3.0 is still in development, but the evolution of Web 2.0 is taking us in that direction

VI. Conclusion

* The World Wide Web has evolved significantly from Web 2.0 to Web 3.0
* New components, architectural changes, and functionality improvements have revolutionized user experiences, scalability, and monetization
* Web 3.0 will continue to build upon these advancements, introducing decentralized services, AI, and enhanced data interoperability



Study Notes:

I. Evolution of Web Architecture

* Web 1.0: Delivering rich content
* Web 2.0: Doing useful things on the Internet
* Shift from server-side to client-side execution
* Inclusion of client devices in the network
* Emergence of single-page applications (SPAs)

II. Single-Page Applications (SPAs)

* Components with individual style, look, and feel
* Coded in JavaScript or TypeScript
* Event-driven architecture
* Event types: time-based, focus-based, click events, etc.

III. Modern Web Architecture




Network Communication and Component Interaction Models:

In this lecture, we delved into the concept of network communication and the various models for component interaction. The following are the key points discussed:

1. **Storing State and Interacting with the Backend:**
	* When dealing with network events, it is essential to have a way to store state, such as what you were looking at and where you were.
	* Components need to interact with the backend, and they can also communicate with each other.
2. **Component Interaction Models:**
	* We discussed various component interaction models, starting with the Callback model.
3. **Callback Model:**
	* Callbacks are functions that you pass to other functions as arguments.
	* When the function you called completes, it gives a way to call back to the parent.
	* In an SPA (Single Page Application) architecture, this is how a parent component talks to a child component.
4. **Promise Model:**
	* The Promise model was introduced to resolve the "callback hell" issue, where multiple nested callbacks could make the code hard to maintain and debug.
	* Promises are objects that represent a failure state when they complete, and they handle asynchronous code more structurally.
	* You can chain everything using the `.then()` and `.catch()` methods to handle errors and log them appropriately.
5. **Async/Await:**
	* The Async/Await model is an evolution of Promises, built on top of them.
	* It allows you to write synchronous-looking code that is actually asynchronous, making it easier to debug and maintain.
	* The `await` keyword is used to pause the execution until the promise completes.
6. **Flux and Cloud Native Architectures:**
	* Facebook's Flux pattern is an evolution of the Model-View-Controller pattern, using many Async/Await features.
	* It stores the state in a central place called a store, and the dispatcher tells actions what to do based on interactions with the views.
	* This pattern helps solve the problems of too many models communicating with too many views, making it easier to manage and debug over time.

In summary, this lecture focused on the importance of network communication and the various models for component interaction. We discussed the Callback, Promise, and Async/Await models, and how they help manage asynchronous code. Additionally, we explored the Flux pattern, which is an evolution of the Model-View-Controller pattern, and how it is used in cloud-native architectures.



Study Notes:

Cloud architectures, such as AWS, Azure, and Google, have been expanded to include mobile apps, browsers, and IoT devices, with security measures in place to protect data as it passes through firewalls and an API gateway. This is based on the Kubernetes model and allows for the management of specific application features and data APIs through configurations.

Web 2.0 has enabled the development of complex web native architectures, with concerns including network security, authentication, data encryption, and the prevention of suspicious traffic. Web Application Firewalls (WAF) have been implemented to protect against threats such as denial of service attacks and SQL injection.

As we move towards Web 3.0, there is a shift towards technologies such as AI, VR, and blockchain. Web 2.0 saw the evolution of architectures used by companies such as Google, Facebook, Netflix, and Amazon, as well as banks, insurance companies, and entertainment providers, who have developed creative APIs to support multiple front-ends.

In terms of security, the traditional method of authenticating and authorizing users based on proxy servers and LDAP credentials is being replaced by the OAuth model. This model is token-based, with tokens used for authorization after the user is authenticated. The OAuth model is secure, fast, and efficient, and is widely used today.

The OAuth model involves several components, including the client, API gateway, API gateway for accessing specific APIs, and an identity provider for authenticating the user and providing appropriate tokens for authorization. All 2.0 requests are initiated by the client, whether it is a mobile app, smart TV, or desktop.

In summary, the lecture covered the evolution of web architectures, from Web 1.0 to Web 2.0 and now Web 3.0, with a focus on the security measures that have been implemented to protect data and authenticate users. The OAuth model was discussed as a secure and efficient method for authorization in web architectures.



Study Notes:

I. OAuth Architecture and Authorization Process

* The OAuth architecture involves a detailed sequence of interactions between components for authorization and authentication.
* The user is authenticated by the authorization server, which also determines the scope of authorization.
* A token is issued to the user, containing authentication and authorization information, which is then used to interact with web services or APIs.
* The token has a time limit and needs to be refreshed periodically.

II. Component Interactions and Sequence of Calls

* The OAuth architecture diagram illustrates the sequence of calls between components, providing a clear understanding of the interactions and use cases.
* The optimization in the architecture involves caching public keys to improve response time and reduce the need to access the identity provider repeatedly.

III. Evolution of Web Architecture

* The transition from Web 2.0 to Web 3.0 involves the replacement of semantic web with AIML models, offering deeper personalization and relevance based on context.
* Web 3.0 aims to connect things based on presence, without requiring hardware or software deployment.
* The Web 3.0 architecture focuses on improving security, removing restrictions associated with specific hardware and software, and decentralizing communication.

IV. Healthcare Authorization Example

* In the context of healthcare, the Web 3.0 architecture aims to simplify the authorization process by turning the complex backend systems into a black box, using blockchain technology.
* This approach removes the restrictions associated with specific hardware and software, streamlining the authorization process in healthcare and other industries.

In summary, the lecture discussed the intricacies of the OAuth architecture, the optimization of caching public keys, and the evolution of web architecture from Web 2.0 to Web 3.0. The Web 3.0 architecture aims to improve security, remove restrictions associated with specific hardware and software, and decentralize communication. The potential of Web 3.0 in simplifying authorization processes, such as in healthcare, was also highlighted.



Study Notes:

Topic: Review of Blockchain and Preparation for Upcoming Lab

In this lecture, the instructor provides an overview of blockchain technology and prepares students for the upcoming lab. The instructor mentions that there may be too much detail on blockchain in this lecture and that a more specific data lecture will be provided in the later stages of the course.

Fungibles are discussed, but the instructor mentions that they are not a real thing anymore. The slides used in the lecture are a bit dated, which is why the lecture is shorter than usual.

The instructor opens the floor for questions and Zak Seipel asks if there is anything missing if he were to start on the Firecracker paper today. The instructor mentions that the YouTube videos and talk are detailed enough for students to start on it standalone. The next step due is the software architecture code.

Zak Seipel confirms that he has already taken care of the software architecture code and thanks the instructor. The instructor reminds students that they can reach him at Discord or send him an email with questions. He mentions that he has not gotten back to students on the spark thing yet, but he will by the end of the course.

The instructor reminds students to send him an email if they have any questions and wishes them good luck with their labs. The lecture ends with Saima Islam thanking the instructor.

Key Points:

* Blockchain technology overview
* Upcoming lab preparation
* Fungibles are not a real thing anymore
* Slides are a bit dated
* Instructor opens the floor for questions
* Firecracker paper can be started today
* Software architecture code is the next step due
* Instructor can be reached at Discord or email for questions
* Instructor will get back to students on the spark thing by the end of the course

Concepts:

* Blockchain technology
* Fungibles
* Labs
* Firecracker paper
* Software architecture code
* Discord
* Spark thing

This lecture provides an overview of blockchain technology and prepares students for the upcoming lab. The instructor mentions that the slides are a bit dated and that fungibles are not a real thing anymore. The instructor opens the floor for questions and answers Zak Seipel's question about starting the Firecracker paper today. The next step due is the software architecture code. The instructor reminds students that they can reach him at Discord or email for questions. The instructor wishes students good luck with their labs and reminds them to send him an email if they have any questions.

Keywords: Blockchain, technology, lab, preparation, fungibles, slides, dated, instructor, questions, Firecracker, paper, software, architecture, code, Discord, email, spark.