import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-configuration',
  templateUrl: './configuration.component.html',
  styleUrl: './configuration.component.css'
})
export class ConfigurationComponent {
    constructor(private http: HttpClient) { }

    addConfiguration(domainURL: string, articlesXpath: string, title: string, body: string, author: string, date: string): void {
      const requestBody = {
        domainURL,
        articlesXpath,
        title,
        body,
        author,
        date
      };
  
      this.http.post('http://127.0.0.1:8080/api/site', requestBody, { responseType: 'text' }) 
        .subscribe(
          (response) => {
            console.log('POST request sent successfully!', response);
            this.clearInputFields();
            window.alert("Site configuration added successfully");
  
  
          },
          (error) => {
            console.log('Error sending POST request:', error);
            alert("Can't connect to API gateway")
        
          }
        );
    }
    clearInputFields(): void {
      // Clear input fields by resetting their values to an empty string
      const inputFields = ['domainURL', 'articles_xpath', 'title', 'body', 'author', 'Date'];
      console.log("Clearing fields");
      inputFields.forEach(field => {
        const inputElement = document.getElementById(field) as HTMLInputElement;
        if (inputElement) {
          inputElement.value = '';
        }
      });
    }
  
}
