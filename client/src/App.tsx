import React from 'react';
import { StyledEngineProvider } from '@mui/material/styles';
import './App.scss';
import Menu from './components/Menu';

function App() {
  return (
    <StyledEngineProvider injectFirst>
      <Menu />
    </StyledEngineProvider>
  );
}

export default App;
