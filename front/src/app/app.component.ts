import { Component } from '@angular/core';
import { Router } from '@angular/router'; // Import Router

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
    constructor(public router: Router) {}
  
    navigateToOverview(): void {
      this.router.navigate(['/']);
    }
  
    navigateToConfiguration(): void {
      this.router.navigate(['/configuration']);
    }
  
}
