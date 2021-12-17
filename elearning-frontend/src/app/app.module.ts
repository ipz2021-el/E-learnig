import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ClarityModule } from '@clr/angular';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import '@cds/core/icon/register.js';
import { ClarityIcons, userIcon, cogIcon, eventIcon, homeIcon, plusCircleIcon } from '@cds/core/icon';
import { CourseComponent } from './course/course.component';
import { DashboardComponent } from './dashboard/dashboard.component';

ClarityIcons.addIcons(userIcon, cogIcon, eventIcon, homeIcon, plusCircleIcon);

@NgModule({
  declarations: [
    AppComponent,
    CourseComponent,
    DashboardComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ClarityModule,
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
