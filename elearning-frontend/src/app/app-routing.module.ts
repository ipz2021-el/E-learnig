import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CourseComponent } from './course/course.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { LessonComponent } from './lesson/lesson.component';
import { CoursesComponent } from './courses/courses.component';
import { AssignmentsComponent } from './assignments/assignments.component';
import { ChatComponent } from './chat/chat.component';
import { QuizComponent } from './quiz/quiz.component';
import { CreateCourseComponent } from './create-course/create-course.component';
import { CreateQuizComponent } from './create-quiz/create-quiz.component';
import { QuizzesComponent } from './quizzes/quizzes.component';

const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'courses', component: CoursesComponent },
  { path: 'course/:id', component: CourseComponent },
  { path: 'course/:id/lesson', component: LessonComponent },
  { path: 'create/course', component: CreateCourseComponent },
  { path: 'assignments', component: AssignmentsComponent },
  { path: 'chat', component: ChatComponent},
  { path: 'quiz/:id', component: QuizComponent },
  { path: 'create/quiz', component: CreateQuizComponent },
  { path: 'quizzes', component: QuizzesComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
