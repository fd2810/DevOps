import React, { useEffect, useState } from 'react';

export default function App() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/api/students') // Adjust port/endpoint to match your backend
      .then((res) => {
        if (!res.ok) throw new Error('Failed to fetch students');
        return res.json();
      })
      .then((data) => {
        // Handle both raw arrays and { students: [...] } responses
        setStudents(Array.isArray(data) ? data : data.students || []);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <h2>Loading students...</h2>;
  if (error) return <h2>Error: {error}</h2>;

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>Student Management</h1>
      <table border="1" cellPadding="8" style={{ borderCollapse: 'collapse', width: '100%' }}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Course</th>
          </tr>
        </thead>
        <tbody>
          {students.length > 0 ? (
            students.map((student) => (
              <tr key={student.id}>
                <td>{student.id}</td>
                <td>{student.name}</td>
                <td>{student.email}</td>
                <td>{student.course}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4" style={{ textAlign: 'center' }}>No students found.</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}