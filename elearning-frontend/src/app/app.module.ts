import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ClarityModule } from '@clr/angular';
import { CdsModule } from '@cds/angular';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import '@cds/core/icon/register.js';
import { ClarityIcons, userIcon, cogIcon, eventIcon, homeIcon, plusCircleIcon } from '@cds/core/icon';
import { CourseComponent } from './course/course.component';
import { DashboardComponent } from './dashboard/dashboard.component';

import '@cds/core/alert/register.js';
import '@cds/core/progress-circle/register.js';
import '@cds/core/button/register.js';
import { LessonComponent } from './lesson/lesson.component';
import { VideoComponent } from './video/video.component';
import { YouTubePlayerModule } from '@angular/youtube-player';

ClarityIcons.addIcons(userIcon, cogIcon, eventIcon, homeIcon, plusCircleIcon);

@NgModule({
  declarations: [
    AppComponent,
    CourseComponent,
    DashboardComponent,
    LessonComponent,
    VideoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ClarityModule,
    BrowserAnimationsModule,
    CdsModule,
    YouTubePlayerModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
