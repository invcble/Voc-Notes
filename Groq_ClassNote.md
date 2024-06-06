Web Architectures
===============

Web architectures have evolved significantly over time, starting from TCP/IP in the 1960s and evolving into the modern-day Internet. The progression of web architectures has been remarkable, with significant advancements since Tim Berners-Lee introduced the World Wide Web in 1989.

Web architectures can be categorized into three generations:

- **Web 1.0 (1990 - early 2000s):** A read-only web architecture where a web browser made a request to a web server, and a file system held onto Jpegs, Gifs, and HTML files to render the web page.
- **Web 2.0 (early 2000s - present):** A read-write web architecture that introduced dynamic content, user interaction, and social media.
- **Web 3.0 (emerging):** Also known as the semantic web, Web 3.0 is characterized by the use of blockchain, AI, VR, and AR.

Common Gateway Interface (CGI) and REST
-------------------------------------

The Common Gateway Interface (CGI) was introduced to allow the running of scripts, which evolved into other mechanisms such as the REpresentational State Transfer (REST) architecture. REST is a software architectural style that defines a set of constraints to be used for creating web services.

RESTful web services are stateless, meaning that each HTTP request from a client to a server must contain all the information needed to understand and process the request. RESTful web services use HTTP methods to perform CRUD operations:

- **POST:** used to create new resources.
- **GET:** used to retrieve resources.
- **PUT:** used to update resources.
- **DELETE:** used to delete resources.

RESTful web services also use URIs to identify resources. URIs stand for Uniform Resource Identifiers. A URI is a string of characters that unambiguously identifies a particular resource on the Internet.

CGI Framework and Web Architecture Evolution
--------------------------------------------

The Common Gateway Interface (CGI) is a standard protocol that enables a web server to run programs and scripts in order to generate dynamic content. CGI scripts can be written in various programming languages such as C, C++, Perl, and Python. However, CGI has some limitations, such as performance issues, as it creates a new process for each request, making it not suitable for high-traffic websites.

The evolution of CGI led to the development of Java servlets, PHP, and various web frameworks such as Ruby on Rails, Django, and AngularJS. These technologies provide a more scalable and efficient way of generating dynamic content compared to CGI.

JavaScript and Web Architecture
------------------------------

JavaScript is a programming language that runs on the client-side, i.e., on the web browser. It allows for more dynamic and interactive web pages. With JavaScript, some of the workload can be shifted from the web server to the client-side, resulting in better performance and user experience.

The evolution of web architecture has led to the development of more sophisticated and dynamic web applications. The architecture has evolved from a simple browser-server model to a more complex model involving application servers, load balancers, and caching mechanisms.

Model-View-Controller (MVC) Framework
------------------------------------

The MVC framework is a software design pattern that separates the application logic into three interconnected components: the model, view, and controller. The model represents the data and the business logic, the view represents the user interface, and the controller handles the input and updates the model and view accordingly.

The MVC framework provides a modular and organized way of building web applications. It allows for better code reusability, maintainability, and scalability. The framework can be implemented using various programming languages and web frameworks such as Ruby on Rails, Django, and AngularJS.

Class-Note for Exam
------------------

### End System/Web Server - Ajax and Web 2.0 Architecture

1. **Ajax:** Allows updating a segment of a web page without reloading the entire page. It uses XmlHttpRequest to communicate asynchronously between the browser and the server. Ajax allows for dynamic content and interaction on web pages, improving user experience by reducing load times and providing real-time updates.
2. **Web 2.0 Architecture:** Enables full-featured applications using web protocols and supports multiple clients, such as mobile apps and IoT devices. It has evolved from static web pages (Web 1.0) to dynamic content (Web 2.0) and is now moving towards semantic web and Web 3.0.
3. **Content Distribution Networks (CDNs):** A system of distributed servers that deliver content to users based on their geographical location. CDNs improve load times and reduce bandwidth usage by caching static content, like application code, closer to the user.
4. **Web Application Firewalls (WAF):** Security measures designed to protect web applications from threats, such as denial-of-service attacks and unauthorized access. WAFs are often implemented in cloud environments and can capture firewall rules to prevent malicious traffic from reaching APIs.
5. **Single Page Applications (SPAs):** Web applications that dynamically rewrite the current web page without requiring a full page load. SPAs, like Facebook and Twitter, provide a seamless user experience by loading content as needed and personalizing the user interface.
6. **Web 3.0 and Semantic Web:** The future of web development aims to create a web that is more intelligent, intuitive, and connected. Web 3.0 incorporates features like artificial intelligence, machine learning, and natural language processing to provide a more personalized user experience.
7. **Architecture Evolution:** The evolution of web architecture has moved from simple static pages to complex, interactive, and personalized user experiences. This evolution has been driven by the need for monetization, user engagement, and the rise of IoT devices and mobile applications.

By understanding these key concepts and the evolution of end systems and web servers, you will be better prepared for the exam and have a solid foundation for further study in web development and architecture.

### Web 2.0 Architecture and Evolution

The lecture focused on the evolution of web architecture, with a focus on Web 2.0 and its impact on various industries such as banking, insurance, and entertainment. The evolution of APIs to support multiple front-ends, such as mobile phones, browsers, and watches, was discussed. The lecture also covered the security aspect of Web 2.0, highlighting the weaknesses of the user ID and password model and the evolution to the OAuth model.

Key Takeaways:

- Web 2.0 architecture has enabled the evolution of various industries by providing support for multiple front-ends through APIs.
- The user ID and password model of security has weaknesses and has evolved to the OAuth model.

### OAuth Model

The lecture then moved on to the OAuth model, which is a token-based model for authorization. The components involved in the OAuth model are the client, API gateway, API running on web services, and the identity provider. The client requests authorization by supplying a client ID and secret, and in return, receives a token that can be used to access resources.

Key Takeaways:

- The OAuth model is a token-based model for authorization.
- The components involved in the OAuth model are the client, API gateway, API running on web services, and the identity provider.

### Web 3.0 Architecture

The lecture concluded by discussing Web 3.0 architecture, which is the evolution of Web 2.0. The focus of Web 3.0 is to decentralize communication, remove restrictions of specific software and hardware components, and improve security architecture.

Key Takeaways:

- Web 3.0 architecture is the evolution of Web 2.0.
- The focus of Web 3.0 is to decentralize communication, remove restrictions of specific software and hardware components, and improve security architecture.

Overall, the lecture provided a good overview of the evolution of web architecture, with a focus on Web 2.0 and its impact on various industries. The lecture also covered the security aspect of Web 2.0 and the evolution to the OAuth model. The lecture concluded by discussing Web 3.0 architecture and its focus on decentralizing communication and improving security architecture.