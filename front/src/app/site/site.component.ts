import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-site',
  templateUrl: './site.component.html',
  styleUrls: ['./site.component.css']
})
export class SiteComponent implements OnInit {
  siteId!: number;

  constructor(private route: ActivatedRoute) {}

  ngOnInit(): void {
    // Retrieve 'id' parameter from the route
    this.route.params.subscribe(params => {
      this.siteId = +params['id']; // Convert 'id' to a number (if it's a number type)
    });
  }
  siteInfo: { domain: string } = { domain: 'Example Site' };

  siteArticles: { url: string, body: string, author: string, date: string }[] = [
    {
      url: 'article1.com',
      body: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
      author: 'John Doe',
      date: '2023-01-01'
    },
    {
      url: 'article2.com',
      body: 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      author: 'Jane Smith',
      date: '2023-01-02'
    },
    {
      url: 'article3.com',
      body: 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
      author: 'Alice Johnson',
      date: '2023-01-03'
    },
    {
      url: 'article4.com',
      body: 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
      author: 'Bob Williams',
      date: '2023-01-04'
    }
  ];
}