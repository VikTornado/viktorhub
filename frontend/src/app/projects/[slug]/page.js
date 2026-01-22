'use client';

import React, { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import { getProject } from '@/lib/api';
import { useLanguage } from '@/context/LanguageContext';
import { ArrowLeft, Github, ExternalLink, Calendar } from 'lucide-react';
import Link from 'next/link';

export default function ProjectDetail() {
  const { slug } = useParams();
  const router = useRouter();
  const { t, lang } = useLanguage();
  const [project, setProject] = useState(null);

  useEffect(() => {
    getProject(slug).then(res => setProject(res.data)).catch(console.error);
  }, [slug]);

  if (!project) return <div className="container-custom py-20">Loading...</div>;

  return (
    <div className="container-custom py-20">
      <button onClick={() => router.back()} className="flex items-center gap-2 text-gray-600 hover:text-blue-600 mb-8 transition-colors">
        <ArrowLeft className="w-4 h-4" />
        {t.projects.back}
      </button>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-12">
        <div className="lg:col-span-2">
          <h1 className="text-4xl md:text-5xl font-bold mb-6">{lang === 'en' ? project.title_en : project.title_uk}</h1>
          
          <div className="flex flex-wrap gap-4 mb-8 text-sm text-gray-500">
            <div className="flex items-center gap-1">
              <Calendar className="w-4 h-4" />
              {new Date(project.created_at).toLocaleDateString()}
            </div>
            <div className="flex flex-wrap gap-2">
              {project.tags.map(tag => (
                <span key={tag.slug} className="px-2 py-0.5 bg-gray-100 dark:bg-gray-800 rounded">#{tag.name}</span>
              ))}
            </div>
          </div>

          <div 
            className="prose prose-lg dark:prose-invert max-w-none"
            dangerouslySetInnerHTML={{ __html: lang === 'en' ? project.description_en : project.description_uk }}
          />
        </div>

        <div className="space-y-8">
          {project.cover_image && (
            <div className="rounded-2xl overflow-hidden border shadow-sm">
              <img src={project.cover_image} alt="" className="w-full h-auto" />
            </div>
          )}

          <div className="bg-gray-50 dark:bg-gray-900 p-6 rounded-2xl border flex flex-col gap-4 transition-colors">
            <h3 className="font-bold border-b pb-2">Tech Stack</h3>
            <p className="text-gray-600 dark:text-gray-400">{project.tech_stack}</p>
            
            <div className="flex flex-col gap-2 mt-4">
              {project.repo_url && (
                <a href={project.repo_url} target="_blank" className="flex items-center justify-center gap-2 bg-black text-white py-3 rounded-xl hover:opacity-80 transition-opacity">
                  <Github className="w-5 h-5" /> GitHub Repo
                </a>
              )}
              {project.live_url && (
                <a href={project.live_url} target="_blank" className="flex items-center justify-center gap-2 bg-blue-600 text-white py-3 rounded-xl hover:bg-blue-700 transition-colors">
                  <ExternalLink className="w-5 h-5" /> Live Demo
                </a>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
