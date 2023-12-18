import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component'; // Import your AppComponent
import { SiteComponent } from './site/site.component'; // Import your SiteComponent
import { SiteOverviewComponent } from './site-overview/site-overview.component';
import { ConfigurationComponent } from './configuration/configuration.component';
const routes: Routes = [
    
  { path: 'configuration', component: ConfigurationComponent }, 
  { path: '', component: SiteOverviewComponent }, 
  { path: 'sites/:id', component: SiteComponent }, 
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
