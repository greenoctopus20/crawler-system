import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-site',
  templateUrl: './site.component.html',
  styleUrls: ['./site.component.css']
})
export class SiteComponent implements OnInit {
  siteId!: number;
  siteInfo: { domain: string } = { domain: 'dutchnews.nl' };
  siteArticles: { url: string, body: string, author: string, date: string }[] = [];

  constructor(private route: ActivatedRoute, private http: HttpClient) {}

  ngOnInit(): void {
    // Retrieve 'id' parameter from the route
    this.route.params.subscribe(params => {
      this.siteId = +params['id']; 
    });

    this.http.get<any[]>('http://127.0.0.1:8080/api/articles') 
    .subscribe(
      (response: any) => {
        console.log(response);  
        console.log(typeof response);

        // Check if response is a string and parse it
        if (typeof response === 'string') {
          response = JSON.parse(response);
        }

        // Check if response is an array before using map
        if (Array.isArray(response)) {
          this.siteArticles = response.map((item) => {
            return {
              url: item.url,
              body: item.body,
              author: item.author,
              date: item.date
            };
          });
        } else {
          console.error('Response is not an array:', response);
        }
      },
      (error) => {
        console.log('Error sending GET request:', error);
      }
    );
  }
}