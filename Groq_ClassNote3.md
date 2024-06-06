Web Architectures
===============

Web architectures have evolved significantly over time, starting from TCP/IP in the 1960s, which laid the foundation for network computers. This eventually evolved into the modern-day Internet. The progression of web architectures has been remarkable, with significant advancements since Tim Berners-Lee introduced the World Wide Web in 1989.

Web architectures can be categorized into three generations:

- **Web 1.0 (1990 - early 2000s):** A read-only web architecture where a web browser made a request to a web server, and a file system held onto Jpegs, Gifs, and HTML files to render the web page.

- **Web 2.0 (early 2000s - present):** A read-write web architecture that introduced the ability for users to interact with web content, including creating and sharing their own content.

- **Web 3.0 (emerging):** Also known as the semantic web, Web 3.0 is characterized by the use of artificial intelligence, blockchain, and other technologies to create more intelligent, interactive, and open web experiences.

Common Gateway Interface (CGI) and REST
---------------------------------------

The Common Gateway Interface (CGI) was introduced to allow the running of scripts, which evolved into other mechanisms today, such as the REST architecture. REST stands for Representational State Transfer, and it is a software architectural style that defines a set of constraints to be used for creating web services.

RESTful web services are stateless, meaning that each HTTP request from a client to a server must contain all the information needed to understand and process the request. The server will not store anything about the latest HTTP request the client made. Each request from any client contains all the information the server needs to service the request.

RESTful web services use HTTP methods to perform CRUD operations. CRUD stands for Create, Read, Update, and Delete. The four HTTP methods used to perform CRUD operations are POST, GET, PUT, and DELETE.

- **POST:** Used to create new resources.
- **GET:** Used to retrieve resources.
- **PUT:** Used to update resources.
- **DELETE:** Used to delete resources.

RESTful web services also use URIs to identify resources. URIs stand for Uniform Resource Identifiers. A URI is a string of characters that unambiguously identifies a particular resource on the Internet.

CGI Framework and Web Architecture Evolution
============================================

Introduction:
------------

Common Gateway Interface (CGI) is a standard protocol that enables a web server to run programs and scripts in order to generate dynamic content. CGI scripts can be written in various programming languages such as C, C++, Perl, and Python. However, CGI has some limitations, such as performance issues, as it creates a new process for each request, making it not suitable for high-traffic websites.

The evolution of CGI led to the development of Java servlets, PHP, and various web frameworks such as Ruby on Rails, Django, and AngularJS. These technologies provide a more scalable and efficient way of generating dynamic content compared to CGI.

CGI and Web Server:
------------------

When a web browser makes a request to a web server, the server processes the request and executes the appropriate CGI script to generate the required content. The script interacts with the database and provides the data back to the web browser. CGI facilitates the communication between the web server and the backend.

JavaScript and Web Architecture:
-------------------------------

JavaScript is a programming language that runs on the client-side, i.e., on the web browser. It allows for more dynamic and interactive web pages. With JavaScript, some of the workload can be shifted from the web server to the client-side, resulting in better performance and user experience.

The evolution of web architecture has led to the development of more sophisticated and dynamic web applications. The architecture has evolved from a simple browser-server model to a more complex model involving application servers, load balancers, and caching mechanisms.

Model-View-Controller (MVC) Framework:
------------------------------------

The MVC framework is a software design pattern that separates the application logic into three interconnected components, i.e., the model, view, and controller. The model represents the data and the business logic, the view represents the user interface, and the controller handles the input and updates the model and view accordingly.

The MVC framework provides a modular and organized way of building web applications. It allows for better code reusability, maintainability, and scalability. The framework can be implemented using various programming languages and web frameworks such as Ruby on Rails, Django, and AngularJS.

Apache Struts:
--------------

Apache Struts is an open-source web application framework for developing Java EE web applications. It is based on the MVC architecture and provides a flexible and customizable way of building web applications. Apache Struts allows for the externalization of configuration files, making it easier to manage and maintain the application.

Web 1.0 and Web 2.0:
--------------------

Web 1.0 was the first generation of the World Wide Web, characterized by static web pages and read-only content. Web 2.0, on the other hand, is the second generation of the World Wide Web, characterized by dynamic and interactive web pages. Web 2.0 provides a more user-centric and participatory web experience, enabling users to interact and collaborate with each other.

Web 2.0 has led to the development of various web technologies such as AJAX, Web Services, and Mashups. These technologies provide a more efficient and interactive way of building web applications.

AJAX:
-----

AJAX (Asynchronous JavaScript and XML) is a web development technique that allows for updating parts of a web page without reloading the entire page. It provides a more seamless and responsive user experience.

AJAX is based on various technologies such as JavaScript, XMLHttpRequest, and XML. It allows for asynchronous communication between the client and the server, enabling the client to request and receive data from the server without reloading the entire page.

Class-Note for Exam
==================

Topic: End System/Web Server - Ajax and Web 2.0 Architecture

1. Ajax: Allows updating a segment of a web page without reloading the entire page. It uses XmlHttpRequest to communicate asynchronously between the browser and the server. Ajax allows for dynamic content and interaction on web pages, improving user experience by reducing load times and providing real-time updates.
2. Web 2.0 Architecture: Enables full-featured applications using web protocols and supports multiple clients, such as mobile apps and IoT devices. It has evolved from static web pages (Web 1.0) to dynamic content (Web 2.0) and is now moving towards semantic web and Web 3.0.
3. Content Distribution Networks (CDNs): A system of distributed servers that deliver content to users based on their geographical location. CDNs improve website performance by reducing the distance between the user and the server, caching content, and balancing the load between servers.
4. Web Application Firewalls (WAF): Security measures designed to protect web applications from threats such as cross-site scripting (XSS), SQL injection, and denial-of-service (DoS) attacks. WAFs are often implemented in cloud environments to secure APIs and prevent unauthorized access.
5. Single Page Applications (SPAs): Web applications that dynamically rewrite the current web page without requiring a full page reload. SPAs provide a seamless user experience by updating content in real-time and reducing the need for page reloads. Examples include Facebook, Twitter, and Gmail.
6. Web 3.0 and Semantic Web: The next generation of web technology focusing on making the web more intelligent, intuitive, and user-friendly. Web 3.0 aims to create a web that understands and responds to user needs by providing personalized, dynamic content based on user behavior and preferences.
7. Architecture Evolution: The evolution of web architecture has moved from static web pages to dynamic content, and now towards semantic web and Web 3.0. This evolution has been driven by the need for monetization, personalization, and user interaction.
8. IoT Devices and Protocols: The growth of IoT devices has led to the development of new communication protocols, such as MQTT, to facilitate communication between devices and web applications. These protocols enable real-time data transfer and efficient management of IoT devices in web applications.
9. Frameworks: Angular and other frameworks have been developed to support the creation of single-page applications, making it easier for developers to build dynamic, user-friendly web applications.

By understanding these concepts, you will be well-prepared for the exam and have a solid foundation in end systems and web server technologies, including Ajax, Web 2.0 architecture, and the evolution towards Web 3.0 and semantic web.

2.0 is that it allowed for more complex and sophisticated web applications, with the use of single page applications (SPAs) and asynchronous JavaScript interactions. This evolution led to the need for more advanced ways to handle asynchronous code, leading to the development of promises and then async/await.

Along with these advancements, the Model-View-Controller (MVC) pattern also evolved, leading to the creation of the Flux pattern used by Facebook. This pattern helps to manage the complexity of multiple models interacting with multiple views by storing the state in a central location called a store.

As we move towards web 3.0, we are seeing even more advanced technologies being integrated into the web, such as artificial intelligence (AI), virtual reality (VR), and blockchain. These technologies are changing the way we interact with the web and will continue to shape its evolution in the future.

Class Notes:
============

Web 2.0 Architecture and Evolution
===================================

The lecture focused on the evolution of web architecture, with a focus on Web 2.0 and its impact on various industries such as banking, insurance, and entertainment. The evolution of APIs to support multiple front-ends, such as mobile phones, browsers, and watches, was discussed. The lecture also covered the security aspect of Web 2.0, highlighting the weaknesses of the user ID and password model and the evolution to the OAuth model.

Key Takeaways:

* Web 2.0 architecture has enabled the evolution of various industries by providing support for multiple front-ends through APIs.
* The user ID and password model of security has weaknesses and has evolved to the OAuth model.

OAuth Model
==========

The lecture then moved on to the OAuth model, which is a token-based model for authorization. The components involved in the OAuth model are the client, API gateway, API running on web services, and the identity provider. The client requests authorization by supplying a client ID and secret, and in return, receives a token that can be used to access resources.

Key Takeaways:

* The OAuth model is a token-based model for authorization.
* The components involved in the OAuth model are the client, API gateway, API running on web services, and the identity provider.

Web 3.0 Architecture
===================

The lecture concluded by discussing Web 3.0 architecture, which is the evolution of Web 2.0. The focus of Web 3.0 is to decentralize communication and remove restrictions of specific software and hardware. The lecture highlighted the use of blockchain technology to improve security architecture and remove restrictions.

Key Takeaways:

* Web 3.0 architecture is the evolution of Web 2.0.
* The focus of Web 3.0 is to decentralize communication and remove restrictions of specific software and hardware.