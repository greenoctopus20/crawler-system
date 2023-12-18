import { Component } from '@angular/core';
import { Router } from '@angular/router'; // Import Router

@Component({
  selector: 'app-site-overview',
  templateUrl: './site-overview.component.html',
  styleUrl: './site-overview.component.css'
})
export class SiteOverviewComponent {
    constructor(private router: Router) {} // Inject the Router

  navigateToSite(id: number): void {
      this.router.navigate([`/sites/${id}`]);
      console.log("navigate");
  }

  title = 'front-end';
  sites = [
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
        // Add more site data as needed
      ];

}
