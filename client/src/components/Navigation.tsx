import { SyntheticEvent, useCallback } from 'react';
import { useDispatch } from 'react-redux'
import BottomNavigation from '@mui/material/BottomNavigation';
import BottomNavigationAction from '@mui/material/BottomNavigationAction';
import FormatListBulletedIcon from '@mui/icons-material/FormatListBulleted';
import CalendarTodayIcon from '@mui/icons-material/CalendarToday';
import PersonIcon from '@mui/icons-material/Person';
import SettingsIcon from '@mui/icons-material/Settings';
import { setPage } from '../stores/feature'

function Navigation() {
  const dispatch = useDispatch();

  const handlePageChange = useCallback((event: SyntheticEvent, page: string) => {
    dispatch(setPage(page));
  }, []);

  // TODO Change to enum
  return (
    <BottomNavigation className="navigation" onChange={handlePageChange}>
      <BottomNavigationAction value="schedule" icon={<FormatListBulletedIcon />} />
      <BottomNavigationAction value="calendar" icon={<CalendarTodayIcon />} />
      <BottomNavigationAction value="profile" icon={<PersonIcon />} />
      <BottomNavigationAction value="settings" icon={<SettingsIcon />} />
    </BottomNavigation>
  );
}

export default Navigation;