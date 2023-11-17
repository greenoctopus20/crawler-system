import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

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

    this.http.post('http://127.0.0.1:8080/api/service1', requestBody)
      .subscribe(
        (response) => {
          console.log('POST request sent successfully!', response);
          // Handle the response here if needed
        },
        (error) => {
          console.log('Error sending POST request:', error);
          // Handle error response or logging here
        }
      );
  }
}
