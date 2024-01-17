import { Component } from '@angular/core';
import { Router } from '@angular/router'; // Import Router
import { KeycloakService } from 'keycloak-angular';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
    constructor(public router: Router, private keycloak: KeycloakService) {}
  
    logout(): void {
        this.keycloak.logout();
      }

    navigateToOverview(): void {
      this.router.navigate(['/']);
    }
  
    navigateToConfiguration(): void {
      this.router.navigate(['/configuration']);
    }
  
}
