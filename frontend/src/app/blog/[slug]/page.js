'use client';

import React, { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import { getPost } from '@/lib/api';
import { useLanguage } from '@/context/LanguageContext';
import { ArrowLeft, Clock, Tag as TagIcon } from 'lucide-react';

export default function BlogPostDetail() {
  const { slug } = useParams();
  const router = useRouter();
  const { t, lang } = useLanguage();
  const [post, setPost] = useState(null);

  useEffect(() => {
    getPost(slug).then(res => setPost(res.data)).catch(console.error);
  }, [slug]);

  if (!post) return <div className="container-custom py-20">Loading...</div>;

  return (
    <div className="container-custom py-20 max-w-4xl">
      <button onClick={() => router.back()} className="flex items-center gap-2 text-gray-600 hover:text-blue-600 mb-8 transition-colors">
        <ArrowLeft className="w-4 h-4" />
        {t.blog.back}
      </button>

      <article>
        <div className="flex items-center gap-4 text-sm text-gray-500 mb-6 transition-colors">
          <div className="flex items-center gap-1"><Clock className="w-4 h-4" /> {new Date(post.published_at).toLocaleDateString()}</div>
          <div className="flex gap-4">
               {post.tags.map(tag => (
                  <span key={tag.slug} className="flex items-center gap-1"><TagIcon className="w-3 h-3" />{tag.name}</span>
                ))}
          </div>
        </div>

        <h1 className="text-4xl md:text-5xl font-bold mb-8 leading-tight">
          {lang === 'en' ? post.title_en : post.title_uk}
        </h1>

        {post.cover_image && (
          <div className="rounded-3xl overflow-hidden mb-12 shadow-xl border">
            <img src={post.cover_image} alt="" className="w-full h-auto" />
          </div>
        )}

        <div 
          className="prose prose-lg dark:prose-invert max-w-none prose-headings:font-bold prose-a:text-blue-600 transition-colors"
          dangerouslySetInnerHTML={{ __html: lang === 'en' ? post.content_en : post.content_uk }}
        />
      </article>
    </div>
  );
}
