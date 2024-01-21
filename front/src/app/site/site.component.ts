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
  domain: string = '';
  siteArticles: { url: string, body: string, title: string, author: string, date: string }[] = [];

  constructor(private route: ActivatedRoute, private http: HttpClient) {}

  exportData(): void {
    // Combine the header and data arrays
    const dataToExport = [
      ['URL', 'title', 'body', 'author', 'date'],
      ...this.siteArticles.map(article => [article.url, article.title, article.body, article.author, article.date])
    ];
  
    // Convert the array to CSV format
    const csvContent = dataToExport.map(row => row.join(',')).join('\n');
  
    // Create a Blob from the CSV content
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  
    // Create a link element and trigger the download
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'exported_data.csv';
    link.click();
  }

  
  ngOnInit(): void {
    // Retrieve 'id' parameter from the route
    this.route.params.subscribe(params => {
      this.siteId = +params['id']; 
    });

    this.http.get<any[]>('http://127.0.0.1:8080/api/articles/' + this.siteId) 
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
            const domainInfo = response.find(item => item.domain);
            if (domainInfo) {
              this.domain = domainInfo.domain.toString();
            }
            
            const filteredArticles = response.filter(item => !item.domain);

            // Map the remaining articles to the siteArticles array
            this.siteArticles = filteredArticles.map(item => {
                return {
                    url: item.url,
                    body: item.body,
                    title: item.title,
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