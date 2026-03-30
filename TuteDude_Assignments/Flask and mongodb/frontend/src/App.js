import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.css';
import Form from './Form/form.jsx';
import Success from './Form/success.jsx';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Form />} />
        <Route path="/success" element={<Success />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
