import { ComponentFixture, TestBed } from '@angular/core/testing';
import { AppComponent } from './app.component';
import { first } from 'rxjs';
import { TodoSignalsService } from './services/todo-signals.service';
import { Todo } from './models/model/todo.model';
import { BrowserAnimationsModule, NoopAnimationsModule } from '@angular/platform-browser/animations';

describe('AppComponent', () => {
  let component: AppComponent;
  let fixture: ComponentFixture<AppComponent>;
  let todoSignalService: TodoSignalsService;

  beforeEach(() => {TestBed.configureTestingModule({imports: [AppComponent, BrowserAnimationsModule, NoopAnimationsModule],providers: [TodoSignalsService]})
    fixture = TestBed.createComponent(AppComponent);
    component = fixture.componentInstance;
    todoSignalService = TestBed.inject(TodoSignalsService);
    fixture.detectChanges();
  
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it('should set @input() property correctly', () => {
    component.projectName = "Testing angular";

    fixture.detectChanges();

    expect(component.projectName).toEqual('Testing angular')
  });

  it("should emit event with @Output() decorator correctly", () => {
    component.projectName = "Testing";
    component.outputEvent.pipe(first()).subscribe({
      next: (event) => {
        expect(event).toEqual('Testing');
        component.handleEmitEvent(component.projectName);
      },
    });
  });

  it("should create new todo correctly and call service method", () => {
    spyOn(todoSignalService, 'updateTodos');
    const newTodo: Todo = {
      id: 1,
      title: 'Testing',
      description: 'Test',
      done: true
    };

    component.handleCreateTodo(newTodo);

    fixture.detectChanges();

    expect(todoSignalService.updateTodos).toHaveBeenCalledWith(newTodo);
    console.log(component.todoSignal());
    // expect(component.todoSignal()).toEqual([newTodo]);
  })

  
});
