import { Component, EventEmitter, Input, OnInit, Output, WritableSignal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './components/header/header.component';
import { TodoCardComponent } from './components/todo-card/todo-card.component';
import { SchoolData, SchoolService } from './services/school.service';
import { Observable, filter, from, map, of, switchMap, zip } from 'rxjs';
import { Todo } from './models/model/todo.model';
import { TodoSignalsService } from './services/todo-signals.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, HeaderComponent, TodoCardComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
  title = 'todo-list-16';
  @Input() public projectName!: string;
  @Output() public outputEvent = new EventEmitter<string>();

  public todoSignal!: WritableSignal<Array<Todo>>;

  constructor(private schoolService: SchoolService, private todoSignalService: TodoSignalsService) {}

  public students: Array<SchoolData> = [];
  public teachers: Array<SchoolData> = [];

  private zipSchoolResponses$ = zip(
    this.getStudentsDatas(),
    this.getTeachersDatas(),
  );

  private ages = of(20, 30, 40, 50, 60, 70);
  private peopleDatas = from([
    {name: 'Marcos Junior', age: 20, profession: 'Software Developer'},
    {name: 'Julia', age: 25, profession: 'UX Designer'},
    {name: 'Jorge', age: 35, profession: 'Scrum Master'},
    {name: 'Sebastião', age:50, profession: 'Software Developer'},
    {name: 'Carla', age: 30, profession: 'Software Developer'}
  ])
  private studentUserId = '2';

  ngOnInit(): void {
    // this.getSchoolDatas();
    // this.getMultipliedAges();
    // this.getPeopleProfessions();
    // this.getSoftwareDevelopersNames();
    // this.handleFindStudentsById();
  }

  handleFindStudentsById() {
    this.getStudentsDatas().pipe(
      switchMap((students) => this.findStudentsById(students, this.studentUserId))
    ).subscribe({
      next: (response) => console.log(response)
    })
  }

  findStudentsById(
    students: Array<SchoolData>,
    userId: string) {
    return from([students.find((students) => students.id === userId)])
  }

  getSoftwareDevelopersNames() {
    this.peopleDatas.pipe(
      filter((people) => people.profession === 'Software Developer'),
      map((people) => people.name)
    ).subscribe({
      next: (response) => console.log(response)
    })
  }

  private getStudentsDatas(): Observable<Array<SchoolData>> {
    return this.schoolService.getStudents();
  }

  private getTeachersDatas(): Observable<Array<SchoolData>> {
    return this.schoolService.getTeachers();
  }

  public getSchoolDatas():void {
    this.zipSchoolResponses$.subscribe({
      next: (response) => {
        console.log('Students', response[0]);
        console.log('Teachers', response[1]);
      }
    })
  }

  public getMultipliedAges():void {
    this.ages.pipe(
      map((age) => age * age)
    ).subscribe({
      next: (response) => {
        console.log('Idade Multiplicada', response);
      }
    })
  }

  public getPeopleProfessions():void {
    this.peopleDatas.pipe(
      map((people) => people.profession)
    ).subscribe({
      next: (response) => {
        console.log('Profissão', response);
      }
    })
  }

  public handleEmitEvent(event: string):void {
    this.outputEvent.emit(event);
  }

  public handleCreateTodo(todo: Todo): void {
    if(todo) {
      this.todoSignalService.updateTodos(todo);
      this.todoSignal = this.todoSignalService.todosState;
    }
  }
}
