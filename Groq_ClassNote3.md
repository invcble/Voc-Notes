Web Architecture Evolution
=========================

The lecture begins with an overview of the evolution of web architectures, starting from TCP/IP in the 1960s, which laid the foundation for networked computers and the modern-day Internet. The instructor then discusses the progression from Web 1.0 to Web 2.0 and the emerging Web 3.0, focusing on the context of this course and the importance of clear documentation and communication of architectural choices.

Web 1.0 (1990)
--------------

* Introduction of HTTP, HTML, and the World Wide Web by Tim Berners-Lee
* Basic web pages using HTML and early forms of Java
* Web 1.0 relied on point-to-point communication between web browsers and web servers

Web 2.0 (1995-Present)
-----------------------

* High-speed communications and native OSs on phones
* Social media, videos, high-quality pictures, and interactive web applications
* Interoperability, AI, VR, and AR examples are emerging in Web 3.0

Web 3.0 (Emerging Standard)
----------------------------

* Semantic web, NFTs, blockchain, and AI
* Interoperability, AI, VR, and AR are key features
* Standards take time to be adopted and agreed upon by different entities

### Read-only web architecture (Web 1.0)

The read-only web architecture (Web 1.0) consists of a web browser making a request to a web server, with the web server responding with content from a file system. The architecture is simple, but it served as the foundation for the more complex and interactive web applications we see today.

### Read-write web architecture (Web 2.0)

In the next section, the lecture will discuss the read-write web architecture (Web 2.0) and its components.

---

Class-Note: Web Architecture and Evolution of CGI
=================================================

Web Architecture and Evolution of CGI
------------------------------------

* Web architecture consists of a web server and a web browser, communicating via requests and responses.
* Static web pages are cacheable and indexable.
* Common Gateway Interface (CGI) is an interface that allows scripts to run on the web server, evolving into mechanisms like React framework.
* CGI scripts can be written in various languages, such as C or C++, and are plugins that run on the web server.
* CGI is not a scalable architecture but was the best solution at the time.
* Web Browser makes a request to the web server, and the CGI script provides the data from the database back to the web browser.
* JavaScript runs on the web browser, evolving the architecture by shifting workload to the client and making web pages more dynamic.

Evolution of CGI:
-----------------

* CGI evolved into Java Servlets, PHP, and different web frameworks like Ruby on Rails and Angular.
* CGI facilitates communication between the web server and the backend.
* JavaScript allows for dynamic web forms and communication with the backend through CGI scripts.

Model View Controller (MVC) and Web Architecture:
----------------------------------------------

* MVC is a way of modularizing service code by shifting code into the web browser, where the view is essentially.
* The view communicates with the model, and the controller, which runs on the application server side, handles actions.
* The Nbc and model view controller pattern provide a lot of dynamic control and configuration-based code execution.

Web 1.0 and Web 2.0:
--------------------

* Web 1.0 existed for 15 years, from 1990 to 2005, and supported read-only content and basic web architectures.
* Web 2.0, starting in 2005, shifted the architecture to allow for running applications or parts of applications on mobile devices or the browser and with Internet of Things.
* Web 2.0 enhanced standards, such as XML, HTTP request, and XHR, enabled running entire applications or parts of applications on mobile devices or the browser.
* Web 2.0 led to the evolution of various applications and VRS.

---

Class-Note on Application Server and Web:
========================================

The lecture discussed the evolution of the web and application servers, focusing on the shift from Web 1.0 to Web 2.0 and the emergence of new technologies such as Ajax and IoT devices.

Web 1.0 consisted of static web pages, while Web 2.0 introduced dynamic content and the ability to run full-featured applications using web protocols. The underlying architecture of Web 2.0 became more complex, with new components such as content providers, content delivery networks (CDNs), and web application firewalls (WAFs).

Ajax and the XHR protocol allowed for asynchronous communication between the web browser and the server, enabling the development of single page applications (SPAs) such as Facebook and Twitter. These SPAs provide a seamless user experience by dynamically updating content without requiring the user to reload the page.

The emergence of IoT devices and the MQTT protocol has allowed for the integration of these devices into web applications. This has led to the development of complex cloud architectures and the use of CDNs to distribute content and improve application performance.

Web 2.0 also introduced new security measures, such as WAFs, to prevent denial of service attacks and protect APIs. These security measures are crucial for protecting web applications and user data.

The evolution of web technologies has allowed for the monetization of web applications, with businesses finding new ways to sell products and services based on user behavior and interactions.

The lecture concluded by mentioning the emergence of Web 3.0 and the semantic web, which aims to provide a more intelligent and intuitive web experience.

---

Key Takeaways:
--------------

* Web 2.0 introduced dynamic content and the ability to run full-featured applications using web protocols.
* Ajax and the XHR protocol allowed for asynchronous communication between the web browser and the server, enabling the development of single page applications (SPAs).
* The emergence of IoT devices and the MQTT protocol has allowed for the integration of these devices into web applications.
* Web 2.0 introduced new security measures, such as WAFs, to prevent denial of service attacks and protect APIs.
* The evolution of web technologies has allowed for the monetization of web applications.
* The emergence of Web 3.0 and the semantic web aims to provide a more intelligent and intuitive web experience.

Actionable Steps:
----------------

* Stay up-to-date with the latest web technologies and trends.
* Consider the use of SPAs and IoT devices in web applications to improve user experience and functionality.
* Implement security measures such as WAFs to protect web applications and user data.
* Explore monetization opportunities in web applications based on user behavior and interactions.
* Keep an eye on the development of Web 3.0 and the semantic web and consider how it may impact web development in the future.