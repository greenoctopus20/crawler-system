import { BrowserModule } from '@angular/platform-browser';
import { APP_INITIALIZER, NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { SiteComponent } from './site/site.component';
import { SiteOverviewComponent } from './site-overview/site-overview.component';
import { ConfigurationComponent } from './configuration/configuration.component';
import { HttpClientModule } from '@angular/common/http';
import { KeycloakAngularModule, KeycloakService } from 'keycloak-angular';
import { initializeKeycloak } from '../app/auth/app.init';
import { RouterModule } from '@angular/router';


@NgModule({
  declarations: [
    AppComponent,
    SiteComponent,
    SiteOverviewComponent,
    ConfigurationComponent
  ],
  imports: [
    BrowserModule,
    RouterModule,
    AppRoutingModule,
    NgbModule,
    HttpClientModule,
    KeycloakAngularModule
  ],
  providers: [HttpClientModule,   {
    provide: APP_INITIALIZER,
    useFactory: initializeKeycloak,
    multi: true,
    deps: [KeycloakService],
  },],    
  bootstrap: [AppComponent]
})
export class AppModule { }