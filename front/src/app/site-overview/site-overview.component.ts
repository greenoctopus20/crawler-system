import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'; // Import Router
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-site-overview',
  templateUrl: './site-overview.component.html',
  styleUrl: './site-overview.component.css',
})
export class SiteOverviewComponent implements OnInit {
  constructor(private router: Router, private http: HttpClient) {}

  navigateToSite(id: number): void {
    this.router.navigate([`/sites/${id}`]);
    console.log('navigate');
  }
  sites: any[] = [];

  ngOnInit(): void {
    this.http.get<any[]>('http://127.0.0.1:8080/api/getSites') 
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
          this.sites = response.map((item) => {
            return {
              id: item.id,
              domain: item.domain,
              articlesExtracted: item.articlesExtracted,
              failedArticles: item.failedArticles,
              lastExtracted: item.lastExtracted
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

  title = 'front-end';
  /* sites = [
        {
          id: 1,
          domain: 'example1.com',
          articlesExtracted: 120,
          failedArticles: 5,
          lastExtracted: '2023-12-15'
        },
        {
          id: 2,
          domain: 'sample2.org',
          articlesExtracted: 80,
          failedArticles: 10,
          lastExtracted: '2023-12-14'
        },
        {
          id: 3,
          domain: 'testsite3.net',
          articlesExtracted: 200,
          failedArticles: 2,
          lastExtracted: '2023-12-12'
        },
        {
          id: 4,
          domain: 'demo4.io',
          articlesExtracted: 50,
          failedArticles: 8,
          lastExtracted: '2023-12-10'
        }
      ]; 
 */
}
