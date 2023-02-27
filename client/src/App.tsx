import { useSelector } from 'react-redux'
import './App.scss';
import { RootState } from './stores/store';
import Navigation from './components/Navigation';
import Schedule from './pages/Schedule';
import Calendar from './pages/Calendar';
import Profile from './pages/Profile';
import Settings from './pages/Settings';

function App() {
  const page = useSelector((state: RootState) => state.page.value)
  
  return (
    <>
      {{
        schedule: <Schedule />,
        calendar: <Calendar />,
        profile: <Profile />,
        settings: <Settings />
      }[page]}
      <Navigation />
    </>
  );
}

export default App;
