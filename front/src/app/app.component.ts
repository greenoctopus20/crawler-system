import { Component } from '@angular/core';
import { Router } from '@angular/router'; // Import Router
import { KeycloakService } from 'keycloak-angular';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
    constructor(public router: Router, private keycloak: KeycloakService, private http: HttpClient) {}
    
    delete_user_data(): void {
        const result = window.confirm('Are you sure you want to perform this action?');

        if (result) {
            const username = this.keycloak.getUsername();
            const requestBody = {
                username : username
            };
            this.http.post('http://127.0.0.1:8080/api/user/delete', requestBody, { responseType: 'text' }) 
            .subscribe(
                (response: any) => {
                    window.location.reload();
                },
                (error) => {
                console.log("Couldn't delete user data")
                }
        );
         
        } else {
          console.log("not deleted");
        }
        const username = this.keycloak.getUsername();
        const requestBody = {
            username : username
        };
        this.http.post('http://127.0.0.1:8080/api/user/delete', requestBody, { responseType: 'text' }) 
        .subscribe(
            (response: any) => {
                //alert("username posted");
            },
            (error) => {
            //alert("username not posted");
            }
        );
    }

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
