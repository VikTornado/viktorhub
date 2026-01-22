'use client';

import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { getNotes } from '@/lib/api';
import { useLanguage } from '@/context/LanguageContext';
import { StickyNote, Tag as TagIcon } from 'lucide-react';

export default function NotesPage() {
  const { t, lang } = useLanguage();
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    getNotes().then(res => setNotes(res.data.results));
  }, []);

  return (
    <div className="container-custom py-20">
      <h1 className="text-4xl font-bold mb-12">{t.notes.title}</h1>
      
      <div className="columns-1 md:columns-2 lg:columns-3 gap-8 space-y-8">
        {notes.map((note, index) => (
          <motion.div 
            key={note.id}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.05 }}
            className="break-inside-avoid p-6 bg-yellow-50 dark:bg-gray-800 border-l-4 border-yellow-400 rounded-r-2xl shadow-sm hover:shadow-md transition-shadow"
          >
            <div className="flex items-center gap-2 mb-3 text-yellow-600 dark:text-yellow-400">
              <StickyNote className="w-5 h-5" />
              <span className="font-bold uppercase tracking-tight text-sm">
                {lang === 'en' ? note.title_en : note.title_uk}
              </span>
            </div>
            <p className="text-gray-700 dark:text-gray-300 whitespace-pre-wrap mb-4">
              {lang === 'en' ? note.content_en : note.content_uk}
            </p>
            <div className="flex flex-wrap gap-2">
              {note.tags.map(tag => (
                <span key={tag.slug} className="text-[10px] text-gray-500 flex items-center gap-0.5">
                  <TagIcon className="w-3 h-3" /> {tag.name}
                </span>
              ))}
            </div>
            <div className="mt-4 text-[10px] text-gray-400">
              {new Date(note.created_at).toLocaleDateString()}
            </div>
          </motion.div>
        ))}
      </div>
    </div>
  );
}
