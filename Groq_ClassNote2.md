



Web Architecture Evolution:

The lecture discusses the evolution of web architectures, starting from TCP/IP in the 1960s, which laid the foundation for networked computers and the modern-day Internet. The focus is on how these architectures have progressed over time and how they have been documented and communicated.

1. Web 1.0 (1990s): This era marked the beginning of the World Wide Web, with the introduction of HTTP and HTML. Web pages were primarily static, and the primary mode of interaction was request-response between web browsers and web servers.
2. Web 2.0 (2000s): The current era of web development, characterized by dynamic, interactive, and social media-driven websites. High-speed communications, cloud access, and native operating systems on mobile devices are integral to Web 2.0.
3. Web 3.0 (Emerging): This future version of the web aims for interoperability, AI integration, and virtual/augmented reality. While examples of Web 3.0 technologies exist, such as NFTs, blockchain, and AI, the standard has not been widely adopted.

Documenting and Communicating Architectures:

The lecture emphasizes the importance of clear documentation and communication of architectural choices. Architecture Decision Records (ADRs) are introduced as a means to document and communicate these choices effectively. ADRs should be based on an existing architecture and should not be created in isolation.

ADR Example:

An ADR example is provided, comparing the use of Kubernetes and AWS Lambda. The decision is based on the consideration of cold start issues and the logic behind the choice. This example demonstrates how ADRs can help document and communicate architectural decisions.

Lab Clarification:

The instructor encourages students to ask questions as they go through the lecture and ensures that the labs are clear.

Key Takeaways:

1. Web architectures have evolved from TCP/IP in the 1960s to Web 1.0, Web 2.0, and the emerging Web 3.0.
2. Clear documentation and communication of architectural choices are essential for successful project execution.
3. Architecture Decision Records (ADRs) can help document and communicate these choices effectively.
4. ADRs should be based on an existing architecture and should not be created in isolation.



Web Architecture Evolution
------------------------

The lecture begins by discussing the importance of understanding web architectures and their evolution over time. The focus is on the clarity and documentation of techniques used in specific architectures rather than the details of how they work. The evolution of web architectures is traced back to the 1960s with the advent of TCP/IP, which laid the foundation for network computers and the modern Internet.

The lecture then moves on to discuss the progression of web architectures, starting from web 1.0, which was characterized by basic web pages built using HTML and early forms of Java. The adoption of web 1.0 started in the mid-90s, and it was marked by static web pages with limited interactivity.

Web 2.0, which is the current state of the web, is characterized by high-speed communications, social media, native operating systems running on phones, and high-quality videos and pictures. Web 2.0 relies on high-speed communications and the ability to access data from anywhere in the world quickly.

The lecture then introduces web 3.0, which is still emerging and includes concepts such as the semantic web, blockchain, AI, VR, and AR. While there are examples of web 3.0 technologies, it will take time for the standard to be adopted and agreed upon by different entities.

Web 1.0 Architecture
--------------------

The lecture then discusses the web 1.0 architecture, which is a request-response model where a web browser makes a request to a web server, and a file system holds onto Jpegs, Gifs, and HTML files to render the web page. There is no dynamic content or interaction with the user in this model.

The Common Gateway Interface (CGI) was introduced to allow the running of scripts in the web architecture. CGI scripts provide data from the database to the web browser. While CGI was a significant improvement, it was not a scalable architecture.

The evolution of CGI includes Java servlets, PHP, and different web frameworks such as the Angular framework and Ruby on Rails. CGI facilitates communication between the web server and the backend.

JavaScript was introduced to run on the web browser, making web pages more dynamic and shifting some of the workload from the web server to the client. This resulted in improved performance and more dynamic web pages.

In summary, the lecture discusses the evolution of web architectures from web 1.0 to web 3.0. The lecture highlights the importance of understanding the progression of web architectures and the clarity and documentation of techniques used in specific architectures. The lecture also discusses the request-response model of web 1.0 architecture and the introduction of CGI and JavaScript to improve web page interactivity and performance.



Study Notes:

Subject: Evolution of Web Architecture

1. Static Web (1.0)
	* Simple request-response model
	* Web server sends back static content (HTML, JPEGs, etc.)
	* No dynamic content, no interaction with the user
	* Basic web architecture

2. Common Gateway Interface (CGI)
	* Allows running of scripts on the web server
	* Evolved into mechanisms like React framework
	* CGI scripts can be written in various languages, including C
	* Not a scalable architecture but the best available at the time

3. Dynamic Web
	* Web browser makes a request to the web server
	* CGI script provides data from the database back to the web browser
	* High-level picture of communication between web server and backend
	* Evolution of CGI: Java servlets, PHP, web frameworks (e.g., Angular, Rails)

4. JavaScript and Client-side Processing
	* JavaScript runs on the web browser
	* Shifts workload from the web server to the client
	* Makes web pages more dynamic
	* Communication between web server and backend through CGI scripts

5. Model-View-Controller (MVC)
	* Modularization of service code
	* Multiple models, views, and controllers
	* Replacing HTML with markup files for speed
	* Configuration-based code execution

6. Web 1.0 vs. Web 2.0
	* Web 1.0 (1995-2005): Read-only content, basic web architectures, model-view-controller pattern
	* Web 2.0 (2005-present): Dynamic content, support for larger applications, split between front-end and back-end, IoT, VR
	* Enabled by advancements like XML over Http, Gmail, Google Maps, and JavaScript libraries

Key Concepts:

- Static web (Web 1.0) vs. dynamic web (Web 2.0)
- Common Gateway Interface (CGI)
- Model-View-Controller (MVC) pattern
- JavaScript and client-side processing
- Web architecture evolution: from simple request-response to dynamic content and IoT support
- Configuration-based code execution
- Impact of XML over Http, Gmail, and Google Maps on web architecture



Study Notes:

Topic: Evolution of Web Architecture and the Introduction of MVC and Ajax

1. Introduction to MVC (Model-View-Controller) pattern in web development:
   - The application server hosts the controller, which manages the actions and communicates with the model.
   - The model updates or refreshes the view based on the data.
   - This modularization allows for larger applications with multiple models, controllers, and views.
   - Replacing HTML with markup files enhances speed and dynamic control, enabling configuration-based code execution.

2. Challenges of MVC and configuration file management:
   - As applications become more complex, configuration files become harder to manage.

3. Web 1.0 and its evolution:
   - Web 1.0, which existed from 1995 to 2005, started with read-only content and evolved to support reasonable-sized applications with basic web architectures using the MVC pattern.

4. The shift to Web 2.0:
   - Web 2.0, introduced in 2005-2006, aimed to simplify the architecture by allowing applications or parts of applications to run on mobile devices or browsers and with Internet of Things.
   - This shift led to applications split between many layers, potentially running all in the front-end client-side, with data and API calls happening in the back-end.

5. The role of Ajax (Asynchronous JavaScript and XML) in Web 2.0:
   - Ajax allows for asynchronous communication between the web browser and web server, updating specific segments of a web page without reloading the entire page.
   - Ajax uses XHR (XMLHttpRequest) to make background data requests and update the web page dynamically.
   - Ajax enables a better user experience by reducing load times and providing real-time updates.

6. Comparing Web 1.0 and Web 2.0:
   - Web 1.0 consisted of static web pages with dynamic content, while Web 2.0 allows for running full-featured applications using web protocols and supports multiple clients, including mobile apps and IoT devices.

By understanding these concepts, you will be able to appreciate the evolution of web architecture, the introduction of MVC and Ajax, and their impact on modern web development.



Study Notes:

Title: Evolution of Web Architecture: From Web 1.0 to Web 2.0 and Beyond

I. Introduction

* Overview of the evolution of web architecture, focusing on the transition from Web 1.0 to Web 2.0 and the emergence of Web 3.0.

II. Web 1.0 (1991 - 2004)

* Static web pages
* HTTP 1.0
* Limited interaction and user engagement

III. Transition to Web 2.0 (2004 - Present)

* Dynamic content
* HTTP 1.1 and HTTP 2: Enhanced payload capabilities
* MQTT: Protocol for IoT device communication
* AJAX: Asynchronous JavaScript and XML for background data processing
* Web application firewalls (WAF) for security
* Content Delivery Networks (CDN) for faster content distribution
* Single Page Application (SPA) architecture: Facebook, Twitter, and other examples
* Personalization and dynamic content based on user interactions
* IoT devices and Bluetooth connectivity

IV. Web 3.0 (The Future)

* Semantic web integration
* Enhanced monetization and user data analysis
* Further advancements in security, scalability, and user experience

V. Key Differences Between Web 2.0 and Web 3.0

* Web 2.0: Focus on user interactions, personalization, and dynamic content
* Web 3.0: Emphasis on semantic web, monetization, and advanced data analysis

VI. Challenges and Opportunities

* Managing complexity in web architectures
* Balancing user privacy and data analysis for monetization
* Leveraging IoT devices and Bluetooth connectivity for scalability

VII. Conclusion

* The evolution of web architecture has significantly transformed the way we interact with the internet, from static web pages to dynamic and personalized content. The future of web architecture promises further advancements in security, scalability, and user experience.



Study Notes:

Subject: Evolution of Web Architecture - From Web 1.0 to Web 3.0

I. Introduction

* Web 3.0 introduced a few years ago
* Progression from Web 1.0 (HTTP 1.0) to Web 2.0 (HTTP 2.0 and MQTT)
* Emphasis on doing useful things over the web

II. Web 2.0 Architecture

* Complex architecture with many new components
* Content Provider: Browser downloads application code from web server or content delivery network (CDN)
* CDN: Provides content quicker by caching it for users
* Web browser, content distribution network, and dynamic application communicate with APIs using Ajax framework
* Web application firewalls for security

III. Single Page Applications (SPA)

* Evolution of web architecture towards SPA
* Facebook, Twitter, and other platforms use SPA architecture
* Personalization and dynamic content based on user interactions
* Monetization as a driving force for development

IV. Web 3.0 and Semantic Web

* Mixed bag of Web 2.0 and Web 3.0 deployments
* Semantic web creeping into Web 2.0 architecture
* IoT devices and various protocols allowing web architecture to scale

V. SPAs and Modern Frameworks

* Introduction of iPhone, Android phones, and frameworks like Angular
* Application code evolving to run on the client
* APIs supporting multiple clients, including IoT devices
* Context of the call driving API runtime and servers

VI. Web 1.0, Web 2.0, and Future Web

* Web 1.0: Delivering rich content
* Web 2.0: Doing useful things on the Internet
* Future web: Running applications locally on the client

VII. Single Page Applications (SPAs)

* Web pages with components that refresh or get more data as the user interacts
* Web components with their own style, look, and feel
* Eventing framework behind the scenes for components to talk to each other or backend systems

VIII. High-Level Architecture Diagrams

* Diagrams communicating the architecture at different levels of detail
* High-level diagrams explaining the overall concept
* Detailed architecture diagrams with components, libraries, and event managers

IX. SPAs and Modern Frameworks

* SPAs can be very complicated
* React, Angular, and other frameworks demonstrate the evolution of SPAs
* Event-driven architecture with various types of events

X. Conclusion

* Web architecture has evolved from simple content delivery to complex, event-driven applications
* Security, personalization, and monetization are key drivers in this evolution
* Understanding the architecture and its components is essential for effective web development



Study Notes:

Title: Evolution of Web Architecture and Component Interaction

I. Introduction

* The evolution of web architecture has led to the development of rich, interactive web applications that can run on various clients, including single-page applications (SPAs), mobile apps, and IoT devices.
* APIs have become crucial in servicing multiple clients and handling data interactions.

II. Web 1.0 vs Web 2.0

* Web 1.0 was about delivering rich content, while Web 2.0 focused on making the Internet useful by enabling interactions and data processing.

III. Single-Page Applications (SPAs)

* SPAs are designed to run application code on the client, allowing for a more interactive user experience.
* Facebook is an example of a web application using SPA technology.

IV. Web Components

* Web components are individual components within a web page, each with its own style, look and feel, and behavior.
* They can be coded in JavaScript or TypeScript and communicate with each other and backend systems using an eventing framework.

V. Event-Driven Architecture

* Event-driven architecture uses events (time-based, focus-based, or click events) to manage state, storage, and interactions with backend systems.

VI. Component Interaction Models

* Component interaction models have evolved from callbacks to promises, and finally to async/await.
* Callbacks: Parent components communicate with child components using functions as arguments.
* Promises: A more structured way to handle asynchronous code and return errors.
* Async/Await: Built on top of promises, async/await allows for writing synchronous code that is executed asynchronously.

VII. Flux Architecture

* Flux is an evolution of the model-view-controller pattern, using features like async/await to manage complex interactions between models and views.
* It stores the state in a centralized "store" and uses a dispatcher to manage actions based on user interactions.

VIII. Cloud-Native Architectures

* Cloud-native architectures are the current standard for web application development, building on the evolution of web architecture and component interaction models.

IX. Conclusion

* The evolution of web architecture has led to the development of rich, interactive web applications using various clients and APIs.
* Component interaction models have become more sophisticated, allowing for better management of asynchronous code and user interactions.
* Cloud-native architectures represent the current state of web application development, building on the lessons learned from previous generations of web architecture.



Study Notes:

Subject: Network Architecture and Component Interaction Models

1. Overview of Network Architecture:
	* Components:
		+ Storage for state and location data
		+ Backend interaction
		+ Component-to-component communication
	* Deeper look into component interaction models:
		+ Callbacks
		+ Promises
		+ Async/Await

2. Callbacks:
	* Functions passed as arguments to other functions
	* Used for parent-child component communication in SPA architecture
	* Example: Parent component calls child component, instructing it to return state upon completion

3. Promises:
	* Evolution of callbacks
	* Addresses "callback hell" issue, where multiple nested callbacks become difficult to maintain and debug
	* Promises represent a state (fulfilled or rejected) and are executed asynchronously
	* Example: Chaining promises to handle asynchronous code and return errors

4. Async/Await:
	* Evolution of Promises
	* Simplifies asynchronous code by allowing synchronous-style syntax
	* Built on top of Promises
	* Example: Using 'await' to pause execution until a Promise completes

5. Flux Architecture:
	* Evolution of Model-View-Controller pattern
	* Uses Async/Await features
	* Stores state in a central location (store)
	* Dispatcher manages actions based on view interactions
	* Example: Facebook's solution for managing complex Model-View-Controller stacks

6. Cloud Native Architectures:
	* API gateways
	* Configuration management
	* Security:
		- Encryption
		- Isolation of traffic
		- Web Application Firewall (WAF)

7. Web 3.0:
	* Artificial Intelligence
	* Virtual Reality
	* Blockchain
	* Evolution of Web 2.0 architectures

8. Security:
	* Authentication and authorization:
		- User ID/password
		- Token-based OAuth model
		- Faster, more efficient, and secure
	* Components:
		- Client
		- API Gateway
		- Web Services Platform
		- Identity Provider



Study Notes:

Title: Evolution of Web Architecture and Security

I. Introduction

* Explanation of the evolution of web architectures in the cloud (AWS, Azure, Google)
* Introduction of the ability to use mobile apps, browsers, IoTs with security in place
* Introduction of the Kubernetes model with an API gateway

II. Web 2.0 Architecture

* Explanation of the complexity of web native architectures
* Discussion of areas of concern such as network, authentication, data security, and component interaction
* Introduction of the Web Application Firewall (WAF) for security

III. Transition to Web 3.0

* Introduction of Web 3.0 and examples of its use (AI, VR, blockchain)
* Comparison of the evolution of Web 2.0 with the emergence of companies like Google, Facebook, Netflix, and Amazon
* Explanation of the evolution of banks, insurance companies, and entertainment providers in support of multiple front ends

IV. Security in Web Architecture

* Explanation of the evolution of authentication and authorization from user ID and password to token-based OAuth model
* Detailed explanation of the components and interactions in the OAuth model (client, API gateway, web services platform, identity provider)
* Explanation of the sequence of calls in the OAuth model (client request, authorization, token issuance, redirection, access to web services)

V. Optimization in Web Architecture

* Explanation of the optimization of caching to improve security and performance
* Explanation of the use of public keys for faster authentication and authorization

VI. Semantic Web and Web 3.0

* Explanation of the replacement of the semantic web with AIml models
* Discussion of the trend towards decentralized communication and the removal of the need for specific hardware and software
* Introduction of the concept of the web being everywhere without the need for deployment

VII. Security in Web 3.0

* Explanation of the focus of Web 3.0 architecture on improving security architecture and removing restrictions
* Discussion of the use of blockchain for trust and component interaction

VIII. Use Cases

* Explanation of the use case of authorization from a healthcare company and the complexity of back-end systems
* Discussion of the goal of turning the complexity into a black box using blockchain technology

Conclusion:

The lecture discussed the evolution of web architectures and security, with a focus on the transition from Web 2.0 to Web 3.0. The lecture explained the complexity of web native architectures, the need for security, and the optimization of caching. The lecture also introduced the concept of the semantic web and the trend towards decentralized communication in Web 3.0. The lecture concluded with a discussion of use cases and the goal of turning complexity into a black box using blockchain technology.



Study Notes:

Title: Authentication and Authorization Architecture, Web 2.0 and Web 3.0

1. Authentication and Authorization Architecture

- The lecture discusses the architecture of authentication and authorization, which involves the client, authorization server, and resource server.
- The client requests access to a resource from the resource server, and the authorization server authenticates the client and grants access based on the scope of authorization.
- The authorization server issues a token to the client, which is then used to interact with the resource server.
- The token has a time limit and needs to be refreshed periodically.

2. Web 2.0 and Web 3.0

- Web 2.0 is the current state of the web, characterized by semantic web and deep personalization based on user context.
- Web 3.0 is the evolution of the web, where actual hardware is replaced by AI models and communication is decentralized.
- The web 3.0 architecture focuses on improving security architecture, removing restrictions of specific hardware and software, and enabling trust based on component interactions.
- The web 3.0 architecture aims to turn complex systems into black boxes, such as healthcare backend systems, by using blockchain technology.

3. Blockchain and Fungibles

- The lecture briefly discusses blockchain and fungibles, but notes that the slides are a bit dated and will be replaced in later lectures.

4. Labs and Next Steps

- The next step for the lab is to work on the software architecture code.
- The lecture recommends starting on the Firecracker paper, as the videos and talk provide enough detail to start.

5. Q&A

- A student asks if they can start on the Firecracker paper, and the instructor confirms that they can.
- The instructor reminds students to reach out via discord or email with questions and notes that he will provide more detail on the spark thing by the end of the course.