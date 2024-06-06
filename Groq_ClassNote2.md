



TOPIC: Web Architecture Evolution

NOTES:

The lecture begins with an overview of the importance of understanding web architectures and how they have evolved over time. The instructor emphasizes the significance of clear documentation and communication of architectural choices and decisions. The lecture covers the progression of web architectures from TCP/IP in the 1960s to the modern-day Internet and the evolution of web 1.0, 2.0, and emerging web 3.0.

1. The foundation: TCP/IP and the early network computers (1960s)
	* The lecture starts by discussing the origins of web architectures, tracing back to the development of TCP/IP in the 1960s, which laid the groundwork for modern networked computers.
2. The birth of the World Wide Web (1989-1990)
	* The lecture then moves on to the introduction of the World Wide Web by Tim Berners-Lee in 1989, with the first real-world utilization of the HTTP protocol starting in 1993-1995.
3. Web 1.0 (1995-2004)
	* Web 1.0 is characterized by basic web pages built using HTML, with early forms of Java and CGI used for web services. This era saw the beginning of the widespread adoption of the web.
4. The rise of Web 2.0 (2004-present)
	* Web 2.0 is marked by the emergence of social media, native operating systems on mobile devices, high-quality videos, and images. The high-speed communication and global access to the cloud are essential features of this era.
5. The Semantic Web and the emergence of Web 3.0
	* The lecture discusses the emergence of Web 3.0, which includes the semantic web, AI, VR, AR, and blockchain technologies. Although examples of these technologies exist, the standard is still evolving and requires agreement among different entities.
6. Read-only web architecture (Web 1.0)
	* In the read-only web architecture of Web 1.0, a web browser makes a request to a web server, which retrieves data from a file system.

The lecture highlights the importance of understanding the historical context and evolution of web architectures. By examining the progression from Web 1.0 to Web 2.0 and the emerging Web 3.0, students can better appreciate the complexities and nuances of modern web architectures.



TOPIC: Evolution of Web Architecture

NOTES:

* Static Web 1.0 (1991-2005): The early days of the web were characterized by static web pages that were primarily read-only. These pages were written in HTML and were served to users upon request. The web server would receive a request from a user's browser, retrieve the corresponding HTML file, and send it back to the browser for rendering. This architecture was simple and easy to implement, but it lacked the dynamic functionality that would come to be expected in later years.
* Model-View-Controller (MVC) and Web 1.5 (2005-2010): As the web evolved, it became clear that a more sophisticated architecture was needed to support the growing demands of web applications. The MVC pattern emerged as a way to organize and manage the complexity of these applications. In this pattern, the application is divided into three main components: the model, which handles data and business logic; the view, which is responsible for rendering the user interface; and the controller, which manages user input and coordinates the interactions between the model and the view. This separation of concerns allowed for greater modularity and scalability in web applications.
* Web 2.0 (2010-present): The current era of web development is characterized by highly dynamic and interactive web applications. The Web 2.0 architecture builds upon the foundations laid by Web 1.0 and Web 1.5, but it takes things to the next level by introducing new technologies and standards that enable rich, real-time interactions between users and web applications. Key technologies in Web 2.0 include AJAX, which allows for asynchronous communication between the browser and the server, and WebSockets, which enables real-time, bidirectional communication.
* The Future of Web Architecture: As the web continues to evolve, it is likely that we will see the emergence of even more sophisticated architectures that build upon the foundations laid by Web 1.0, Web 1.5, and Web 2.0. Some possible directions for the future of web architecture include the use of decentralized, peer-to-peer networks, the integration of artificial intelligence and machine learning, and the development of new standards for real-time, multi-user interactions.

In conclusion, the evolution of web architecture has been marked by a series of incremental improvements and innovations that have built upon the foundations laid by previous generations of web technology. From the simple, read-only pages of Web 1.0 to the rich, interactive applications of Web 2.0, the web has come a long way in its short history. As we look to the future, it is clear that the web will continue to evolve and adapt to meet the changing needs of users and developers alike.



TOPIC: Evolution of Web Technologies - From Web 1.0 to Web 3.0

NOTES:

The lecture begins with an introduction to Ajax, a technology that enables asynchronous communication between the web browser and web server, allowing for dynamic updates of web page components without requiring a full page reload. Ajax uses XHR (XMLHttpRequest) to communicate with the server and is the foundation for many modern web applications.

Web 2.0 is characterized by the shift from static web pages to dynamic, interactive web applications. This evolution was enabled by advancements in web technologies such as Ajax, which allowed for rich user interactions and real-time data updates. Web 2.0 also saw the rise of web application firewalls (WAF) and API gateways for enhanced security and management of web applications.

The architecture of Web 2.0 applications consists of several components, including content providers, content delivery networks (CDNs), web browsers, and dynamic application components. Content providers serve application code, which can be downloaded by the web browser from the web server or a CDN. CDNs help distribute content globally, ensuring faster load times for users by caching and serving content from servers closer to the user's location.

Web 2.0 applications are designed to be dynamic and interactive, with the web browser downloading and executing the application code. The application then communicates with APIs to retrieve data and update the user interface. Web application firewalls are used to secure these applications by enforcing security rules and preventing unauthorized access.

The evolution of web technologies has led to the development of single-page applications (SPAs), such as Facebook and Twitter, where the entire application runs within the web browser, and content is dynamically updated based on user interactions. SPAs provide a seamless user experience, with content loading as needed, rather than requiring full page reloads.

The rise of IoT devices has further expanded the capabilities of web applications, enabling the integration of various devices and systems through standardized protocols such as MQTT. This has allowed for the creation of complex, distributed systems that can scale and adapt to changing user needs.

The lecture concludes by discussing the future of web technologies, with the emergence of Web 3.0. Web 3.0 aims to build on the foundations laid by Web 2.0, focusing on semantic web technologies, decentralized systems, and artificial intelligence. These advancements will enable even more sophisticated and personalized user experiences, with web applications that can better understand and respond to user needs and preferences.

In summary, the evolution of web technologies has transformed the way we interact with the internet, from static web pages to dynamic, interactive web applications. The ongoing development of web technologies promises to continue this trend, with Web 3.0 and beyond, enabling increasingly sophisticated and personalized user experiences.



TOPIC: Evolution of Web Architecture and Component Interaction Models

NOTES:

* The lecture begins by discussing the evolution of web architecture, highlighting the shift from Web 1.0, which focused on delivering rich content, to Web 2.0, which focused on making the Internet more interactive and useful.
* The architecture has evolved to enable running application code on the client-side, allowing for a more seamless user experience. Single-page applications (SPAs) are an example of this evolution, where components of a webpage can refresh or load more data as the user interacts with them.
* Web components are the building blocks of SPAs, with each component having its own style, look and feel, and behavior, which can be coded in JavaScript or TypeScript. These components can communicate with each other and with backend systems through an eventing framework.
* The lecture then moves on to discussing various component interaction models, starting with callbacks. Callbacks are functions that are passed as arguments to other functions, allowing the parent function to call back to the parent when it has completed.
* The promise model was introduced to resolve issues with callbacks, where nesting could become so deep that code became hard to maintain and debug. Promises are objects that represent the eventual completion or failure of an asynchronous operation, allowing for a more structured way to handle asynchronous code.
* Async/await is the evolution of promises, allowing developers to write synchronous-looking code that is actually asynchronous. This makes it easier to debug and maintain asynchronous code.
* The lecture then discusses how these interaction models are used in cloud-native architectures, specifically in the context of the Flux pattern used by Facebook. Flux is an evolution of the Model-View-Controller pattern, using a lot of the Async/await features to manage complex interactions between models and views.
* The Flux pattern stores the state in a central location called a store, and uses a dispatcher to manage actions based on user interactions. This helps to manage and debug complex interactions between models and views.
* The lecture concludes by discussing how these patterns are commonly used in modern web development, specifically in the context of reactive programming and unidirectional data flow. Reactive programming is a programming paradigm that allows developers to build applications that can react to changes in data, while unidirectional data flow helps to manage the complexity of modern web applications.



TOPIC: Evolution of Web Architecture and Security

NOTES:

The lecture discusses the evolution of web architecture, from Web 1.0 to Web 2.0 and now to Web 3.0, and the corresponding advancements in security measures.

Web 2.0 has allowed for complex web native architectures, using mobile apps, browsers, IoT, and APIs, all with security in place. This includes an API gateway that manages access to data APIs and specific application features, with all components managed through configurations. Web 2.0 has enabled a focus on areas of concern such as network security, authentication, data encryption, and isolating suspicious traffic.

The lecture then moves on to discuss the transition from Web 2.0 to Web 3.0, which is still in its early stages but already has many examples in use, such as AI, VR, and blockchain. Web 3.0 is characterized by decentralized communication and the removal of restrictions imposed by specific software and hardware components.

The lecture also touches on the evolution of security measures, from user ID and password authentication to the OAuth model, which is token-based and primarily used for authorization. The OAuth model is secure, fast, and efficient, and involves a client, API gateway, web services platform, and identity provider.

The lecture also discusses the use of caching in Web 2.0 to optimize performance and the use of semantic web in Web 3.0, which will be replaced by AIML models that provide deep personalization and relevance based on context.

The lecture concludes by discussing the potential of Web 3.0 to turn complex healthcare backend systems into a black box using blockchain technology, removing the restrictions imposed by specific hardware and software components.

In summary, the lecture covers the evolution of web architecture, from Web 1.0 to Web 2.0 and now to Web 3.0, and the corresponding advancements in security measures. The lecture highlights the focus on decentralized communication, optimization, and security in Web 3.0, and the potential for blockchain technology to revolutionize healthcare backend systems.