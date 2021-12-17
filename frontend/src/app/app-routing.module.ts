import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { HomeComponent } from './components/home/home.component';
import { DetailsComponent } from './components/profiles/details/details.component';
import { ProfilesComponent } from './components/profiles/profiles.component';
import { AuthGuard } from './guards/auth.guard';
import { ProfilesResolver } from './resolvers/profiles.resolver';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'profiles', component: ProfilesComponent, resolve: { profiles: ProfilesResolver } },
  { path: 'dashboard', component: DashboardComponent, canActivate: [AuthGuard] },
  { path: 'profile/:id', component:DetailsComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
