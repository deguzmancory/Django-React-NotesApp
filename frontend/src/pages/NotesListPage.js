import React, { useState, useEffect } from "react";
import ListItem from "../components/ListItem";

const NotesListPage = () => {
	const [notes, setNotes] = useState([]);

	const getNotes = async () => {
		let response = await fetch("http://localhost:8000/api/notes");
		let data = await response.json();
		setNotes(data);
	};

	useEffect(() => {
		getNotes();
	}, []);

	return (
		<div>
			<div className="notes-list">
				{notes.map((note, index) => (
					// <h3 key={index}>{note.body}</h3>
					<ListItem key={index} note={note} />
				))}
			</div>
		</div>
	);
};

export default NotesListPage;
