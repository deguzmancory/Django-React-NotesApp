import React, { useState, useEffect } from "react";

const NotesListPage = () => {
	const [notes, setNotes] = useState([]);

	const getNotes = async () => {
		let response = await fetch("http://localhost:8000/api/notes");
		let data = await response.json();
		console.log("Data:", data);
		setNotes(data);
	};

	useEffect(() => {
		getNotes();
	}, []);

	return <div>Notes</div>;
};

export default NotesListPage;
