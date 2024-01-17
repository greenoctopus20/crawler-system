import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component'; // Import your AppComponent
import { SiteComponent } from './site/site.component'; // Import your SiteComponent
import { SiteOverviewComponent } from './site-overview/site-overview.component';
import { ConfigurationComponent } from './configuration/configuration.component';
import { AuthGuard } from './auth/app.guard';
const routes: Routes = [
    
  { path: 'configuration', component: ConfigurationComponent, canActivate: [AuthGuard]}, 
  { path: '', component: SiteOverviewComponent, canActivate: [AuthGuard] }, 
  { path: 'sites/:id', component: SiteComponent, canActivate: [AuthGuard] }, 
  
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
